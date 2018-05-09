from contextlib import contextmanager, suppress
from functools import partial
from onegov.core import locking
from onegov.core.custom import custom_json as json
from onegov.core.errors import TooManyInstancesError
from onegov.core.errors import TooManyWorkersError
from onegov.core.framework import Framework
from onegov.core.security import Public
from pycurl import Curl
from threading import Thread
from time import sleep
from uuid import uuid4


@contextmanager
def lock_first(session, namespace, count):
    for n in range(0, count):
        with locking.lock(session, namespace, str(count)):
            yield n


class Worker(object):

    def __init__(self, request, name, token, parameters, session_id):
        self.request = request
        self.name = name
        self.token = token
        self.paramters = parameters or {}
        self.session_id = session_id

    @property
    def registration(self):
        return self.request.app.config.worker_registry[self.name]

    @property
    def function(self):
        return self.registration.function

    @property
    def max_instances(self):
        return self.registration.max_instances

    @property
    def state(self):
        return self.request.worker_cache.get(self.token, None)

    @state.setter
    def state(self, state):
        self.request.worker_cache.set(self.token, state)

    def execute(self):
        lock = partial(lock_first, session=self.request.session)

        try:
            with lock('worker-', self.request.app.max_workers) as n:
                with lock(f'instance-{self.name}-', self.max_instances):

                    self.request.worker_cache[f'worker-{n}'] = self.token
                    self.state = 'started'

                    with self.request.virtual_session_id(self.session_id):
                        try:
                            return self.function(
                                self.request, **self.parameters)
                        finally:
                            del self.request.worker_cache[f'worker-{n}']

        except locking.AlreadyLockedError as e:
            if e.namespace.startswith('worker'):
                self.state = 'too-many-workers'
            elif e.namespace.startswith('instance'):
                self.state = 'too-many-instances'
            else:
                raise NotImplementedError


def spawn_worker(request, name, **params):
    assert name in request.app.config.worker_registry

    def post(url, body):
        c = Curl()
        c.setopt(c.URL, url)
        c.setopt(c.POST, True)
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])

        # ignores the result, returns the number of 'written' bytes
        c.setopt(c.WRITEFUNCTION, len)
        c.setopt(c.POSTFIELDS, json.dumps(body))

        # we really don't care about the result, http is not used for
        # communication at all here
        c.perform()
        c.close()

    # create a token to start the worker in another process
    # (uses a nonce to ensure that each token is unique)
    token = request.new_url_safe_token({
        'name': name,
        'nonce': uuid4.hex()
    })

    body = {
        'session_id': request.session_id,
        'parameters': params
    }

    url = request.class_link(Worker, {'token': token})
    Thread(target=post, args=(url, body)).start()

    # wait for it to be started (we need an id here...)
    timeout = 60
    polling = 0.2
    for i in range(0, timeout / polling):
        with suppress(KeyError):
            status = request.app.worker_cache[f'{token}-status']

            if status == 'started':
                return True
            elif status == 'too-many-workers':
                raise TooManyWorkersError()
            elif status == 'too-many-instances':
                raise TooManyInstancesError()
            else:
                raise NotImplementedError

        sleep(polling)


@Framework.path(model=Worker, path='/workers/{token}')
def load_worker(request, token):
    data = request.load_url_safe_token(token, max_age=60)

    if data:
        assert data['name'] in request.app.config.worker_registry
        return Worker(request, data['name'], token, **json.loads(request.POST))


@Framework.view(model=Worker, permission=Public)
def view_worker(self, request):
    self.execute()
