import requests

from datetime import datetime
from freezegun import freeze_time
from onegov.core import Framework
from onegov.core.utils import scan_morepath_modules
from pytest_localserver.http import WSGIServer
from sedate import replace_timezone
from sqlalchemy.ext.declarative import declarative_base
from time import sleep
from webtest import TestApp as Client


def test_run_cronjob(postgres_dsn, redis_url):
    result = 0

    class App(Framework):
        pass

    @App.path(path='')
    class Root(object):
        pass

    @App.json(model=Root)
    def view_root(self, request):
        return {}

    @App.cronjob(hour='*', minute='*', timezone='UTC', once=True)
    def run_test_cronjob(request):
        nonlocal result
        result += 1

    scan_morepath_modules(App)

    app = App()
    app.configure_application(
        dsn=postgres_dsn,
        base=declarative_base(),
        redis_url=redis_url
    )
    app.namespace = 'municipalities'
    app.set_application_id('municipalities/new-york')

    # to test we need an actual webserver, webtest doesn't cut it here because
    # we are making requests from the application itself
    server = WSGIServer(application=app)

    try:
        server.start()

        with freeze_time(replace_timezone(datetime(2016, 1, 1, 8, 0), 'UTC')):
            requests.get(server.url)

            for i in range(0, 600):
                if result == 0:
                    sleep(0.1)
                else:
                    break

            sleep(0.1)
            assert result == 1

    finally:
        server.stop()


def test_disable_cronjobs(redis_url):

    class App(Framework):
        pass

    @App.path(path='')
    class Root(object):
        pass

    @App.json(model=Root)
    def view_root(self, request):
        return {}

    @App.cronjob(hour=8, minute=0, timezone='UTC')
    def run_test_cronjob(request):
        pass

    @App.setting(section='cronjobs', name='enabled')
    def cronjobs_enabled():
        return False

    scan_morepath_modules(App)

    app = App()
    app.configure_application(redis_url=redis_url)
    app.namespace = 'municipalities'
    app.set_application_id('municipalities/new-york')

    client = Client(app)
    client.get('/')

    assert not app.config.cronjob_registry.cronjob_threads
