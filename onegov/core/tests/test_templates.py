import more.webassets
import onegov.core
import os
import os.path
import polib

from morepath import setup
from onegov.core import Framework
from translationstring import TranslationStringFactory
from webtest import TestApp as Client


def test_chameleon_with_translation(tempdir):
    # Test chameleon in a real scenario with templating and translations

    templates = os.path.join(tempdir, 'templates')
    os.mkdir(templates)

    locale = os.path.join(tempdir, 'locale')
    os.makedirs(os.path.join(locale, 'de/LC_MESSAGES'))

    po = polib.POFile()
    po.append(polib.POEntry(
        msgid=u'Welcome',
        msgstr=u'Willkommen'
    ))
    po.append(polib.POEntry(
        msgid=u"We're sinking, we're sinking!",
        msgstr=u'Wir denken, wir denken!'
    ))
    po.save(os.path.join(locale, 'de/LC_MESSAGES/onegov.test.po'))

    with open(os.path.join(templates, 'index.pt'), 'w') as f:
        f.write("""
            <!DOCTYPE html>
            <html xmlns="http://www.w3.org/1999/xhtml"
                  xmlns:i18n="http://xml.zope.org/namespaces/i18n"
                  xmlns:tal="http://xml.zope.org/namespaces/tal"
                  i18n:domain="onegov.test">
                <b><tal:block i18n:translate="">Welcome</tal:block></b>
                <b>${foo}</b>
            </html>
        """)

    _ = TranslationStringFactory('onegov.test')

    config = setup()

    class App(Framework):
        testing_config = config

    @App.template_directory()
    def get_template_directory():
        class Mock(object):
            pass

        # Morepath should support absolute template directories, but it
        # doesn't do it currently, this seems to be a bug:
        # https://github.com/morepath/morepath/issues/299
        #
        # Until that bug is fixed we corce the caller stack into building
        # the correct path by sheer hackery
        attach_info = Mock()
        attach_info.module = Mock()
        attach_info.module.__file__ = templates

        import inspect
        stack = inspect.stack()
        self = stack[1][0].f_locals['self']
        self.attach_info = attach_info

        return 'templates'

    @App.setting(section='i18n', name='localedir')
    def get_locale_directory():
        return locale

    @App.setting(section='i18n', name='domain')
    def get_i18n_domain():
        return 'onegov.test'

    @App.setting(section='i18n', name='default_locale')
    def get_i18n_default_locale():
        return 'de'

    @App.path(path='/')
    class Root(object):
        pass

    @App.html(model=Root, template='index.pt')
    def view_root(self, request):
        return {
            'foo': _("We're sinking, we're sinking!")
        }

    config.scan(onegov.core)
    config.scan(more.webassets)
    config.commit()

    client = Client(App())
    assert '<b>Willkommen</b>' in client.get('/').text
    assert '<b>Wir denken, wir denken!</b>' in client.get('/').text