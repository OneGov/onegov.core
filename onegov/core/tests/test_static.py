import more.webassets
import onegov.core
import os.path
import time

from morepath import setup
from onegov.core import Framework
from onegov.core.static import StaticFile
from webtest import TestApp as Client


def test_static_file(tempdir):

    class App(object):
        pass

    app = App()
    app.static_files = tempdir

    with open(os.path.join(tempdir, 'robots.txt'), 'w') as f:
        f.write('foobar')

    app.serve_static_files = False
    assert StaticFile.from_application(app, 'robots.txt') is None

    app.serve_static_files = True
    assert StaticFile.from_application(app, 'robots.txt').path == os.path.join(
        app.static_files, 'robots.txt'
    )

    assert StaticFile.from_application(app, '../robots.txt') is None


def test_static_file_app(tempdir):
    config = setup()

    class App(Framework):
        testing_config = config
        serve_static_files = True
        static_files = tempdir

    config.scan(more.webassets)
    config.scan(onegov.core)
    config.commit()

    with open(os.path.join(tempdir, 'robots.txt'), 'w') as f:
        f.write('foobar')

    app = App()
    app.configure_application()

    c = Client(app)
    assert c.get('/static/robots.txt').text == 'foobar'

    # make sure the if-modified-since header is honored
    timestamp = time.gmtime(time.time() + 1)
    modified = time.strftime('%a, %d %b %Y %H:%M:%S GMT', timestamp)
    headers = {'If-Modified-Since': modified}

    response = c.get('/static/robots.txt', headers=headers, expect_errors=True)
    assert response.status_code == 304

    # make sure inexistant files return a 404
    assert c.get('/static/humans.txt', expect_errors=True).status_code == 404


def test_root_file_app(tempdir):
    config = setup()

    class App(Framework):
        testing_config = config
        serve_static_files = True
        static_files = tempdir

    class RobotsTxt(StaticFile):
        pass

    @App.path(model=RobotsTxt, path='robots.txt')
    def get_favicon(app, absorb):
        return StaticFile.from_application(app, 'robots.txt')

    config.scan(more.webassets)
    config.scan(onegov.core)
    config.commit()

    with open(os.path.join(tempdir, 'robots.txt'), 'w') as f:
        f.write('foobar')

    app = App()
    app.configure_application()

    c = Client(app)
    assert c.get('/robots.txt').text == 'foobar'