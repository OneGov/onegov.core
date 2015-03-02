""" Provides caching methods for onegov.core.

Onegov.core uses dogpile for caching:
`<https://dogpilecache.readthedocs.org/>`_

Unlike dogpile onegov.core does not provide a global region however.
The cache regions are available through the app::

    request.app.forever.set('key', 'value')

Global caches in a multi-tennant application are a security vulnerability
waiting to be discovered. Therefore we do not do that!

This means that this won't be available::

    from x import cache
    @cache.cache_on_arguments()
    def my_function():
        return 'foobar'

Syntactic sugar like this will be provided through decorators inside this
module in the future. For example, we could write one that is usable
on all morepath views::

    @App.view(...)
    @cache.view()
    def my_view():
        return '<html>...'

But no such method exists yet.
"""

import pylibmc

from dogpile.cache import make_region
from dogpile.cache.api import NO_VALUE
from dogpile.cache.proxy import ProxyBackend
from onegov.core import log


DEFAULT_BACKEND_ARGUMENTS = {
    'dogpile.cache.pylibmc': {
        'binary': True,
        'behaviors': {
            'tcp_nodelay': True,
            'ketama': True
        }
    }
}


def create_backend(namespace, backend, arguments, expiration_time):

    prefix = '{}:'.format(namespace)

    _arguments = DEFAULT_BACKEND_ARGUMENTS.get(backend, {})
    _arguments.update(arguments)

    return make_region(key_mangler=lambda key: prefix + key).configure(
        backend,
        expiration_time=None,
        arguments=_arguments,
        wrap=[IgnoreUnreachableBackend]
    )


class IgnoreUnreachableBackend(ProxyBackend):
    """ A proxy backend that logs an error when memcached is down, but keeps
    running, albeit without using any caching.

    The idea is that a memcached outage will result in a slower/degraded
    user experience, not in complete breakage.

    """
    def get(self, key):
        try:
            return self.proxied.get(key)
        except pylibmc.Error:
            log.exception("Error reading cache-key '{}'".format(key))
            return NO_VALUE

    def set(self, key, value):
        try:
            self.proxied.set(key, value)
        except pylibmc.Error:
            log.exception("Error writing cache-key '{}'".format(key))

    def delete(self, key):
        try:
            self.proxied.delete(key)
        except pylibmc.Error:
            log.exception("Error deleting cache-key '{}'".format(key))