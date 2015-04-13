import collections

from cached_property import cached_property
from more.webassets.core import IncludeRequest
from onegov.core import utils
from onegov.core.crypto import random_token


Message = collections.namedtuple('Message', ['text', 'type'])


class CoreRequest(IncludeRequest):
    """ Extends the default Morepath request with virtual host support and
    other useful methods.

    Virtual hosting might be supported by Morepath directly in the future:
    https://github.com/morepath/morepath/issues/185

    """

    def link_prefix(self):
        """ Override the `link_prefix` with the application base path provided
        by onegov.server, because the default link_prefix contains the
        hostname, which is not useful in our case - we'll add the hostname
        ourselves later.

        """
        return getattr(self.app, 'application_base_path', '')

    @cached_property
    def x_vhm_host(self):
        """ Return the X_VHM_HOST variable or an empty string.

        X_VHM_HOST acts like a prefix to all links generated by Morepath.
        If this variable is not empty, it will be added in front of all
        generated urls.
        """
        return self.headers.get('X_VHM_HOST', '').rstrip('/')

    @cached_property
    def x_vhm_root(self):
        """ Return the X_VHM_ROOT variable or an empty string.

        X_VHM_ROOT is a bit more tricky than X_VHM_HOST. It tells Morepath
        where the root of the application is situated. This means that the
        value of X_VHM_ROOT must be an existing path inside of Morepath.

        We can understand this best with an example. Let's say you have a
        Morepath application that serves a blog under /blog. You now want to
        serve the blog under a separate domain, say blog.example.org.

        If we just served Morepath under blog.example.org, we'd get urls like
        this one::

            blog.example.org/blog/posts/2014-11-17-16:00

        In effect, this subdomain would be no different from example.org
        (without the blog subdomain). However, we want the root of the host to
        point to /blog.

        To do this we set X_VHM_ROOT to /blog. Morepath will then automatically
        return urls like this::

            blog.example.org/posts/2014-11-17-16:00

        """
        return self.headers.get('X_VHM_ROOT', '').rstrip('/')

    def transform(self, url):
        """ Applies X_VHM_HOST and X_VHM_ROOT to the given url (which is
        expected to not contain a host yet!). """
        if self.x_vhm_root:
            url = '/' + utils.lchop(url, self.x_vhm_root).lstrip('/')

        if self.x_vhm_host:
            url = self.x_vhm_host + url

        return url

    def link(self, *args, **kwargs):
        """ Extends the default link generating function of Morepath. """
        return self.transform(
            super(CoreRequest, self).link(*args, **kwargs))

    def filestorage_link(self, path):
        """ Takes the given filestorage path and returns an url if the path
        exists. The url might point to the local server or it might point to
        somehwere else on the web.

        """

        app = self.app

        if not app.filestorage.exists(path):
            return None

        url = app.filestorage.getpathurl(path, allow_none=True)

        if url:
            return url
        else:
            return self.link(app.modules.filestorage.FilestorageFile(path))

    @cached_property
    def theme_link(self):
        """ Returns the link to the current theme. Computed once per request.

        The theme is automatically compiled and stored if it doesn't exist yet,
        or if it is outdated.

        """
        theme = self.app.registry.settings.core.theme
        assert theme is not None, "Do not call if no theme is used"

        filename = self.app.modules.theme.compile(
            self.app.themestorage, theme, self.app.theme_options,
            force=self.app.always_compile_theme
        )

        return self.link(self.app.modules.theme.ThemeFile(filename))

    @cached_property
    def session_id(self):
        """ Returns a random session id, making sure it's stored in the
        cookies. This random session id is used to access data associated
        with the browser session.

        The random token is very strong and it is signed, making it even harder
        to guess a token used by another user.

        If someone gains access to this session id, all bets are off though.
        To prevent that, cookies should only be transmitted over https.

        See :meth:`onegov.core.framework.Framework.configure_application`.

        """

        sessionid = self.app.unsign(self.cookies.get('sessionid', ''))

        if not sessionid:
            sessionid = random_token()
            self.cookies['sessionid'] = self.app.sign(sessionid)

            @self.after
            def store_session(response):
                response.set_cookie(
                    'sessionid',
                    self.cookies['sessionid'],
                    secure=self.app.identity_secure,
                    httponly=True
                )

        return sessionid

    @cached_property
    def browser_session(self):
        """ Returns a browser_session bound to the request. Works via cookies,
        so requests without cookies won't be able to use the browser_session.

        """

        return self.app.modules.browser_session.BrowserSession(
            namespace=self.app.application_id,
            token=self.session_id,
            cache=self.app.cache
        )

    def get_form(self, form_class):
        """ Returns an instance of the given form class, set up with the
        correct translator and with CSRF protection enabled (the latter
        doesn't work yet).

        """
        translate = self.get_translate(for_chameleon=False)
        form_class = self.app.modules.i18n.get_translation_bound_form(
            form_class, translate)

        return form_class(self.POST, meta={'locales': self.app.languages})

    def get_translate(self, for_chameleon=False):
        """ Returns the translate method to the given request, or None
        if no such method is availabe.

        :for_chameleon:
            True if the translate instance is used for chameleon (which is
            special).

        """
        if not self.app.languages:
            return None

        settings = self.app.registry.settings

        locale = settings.i18n.locale_negotiator(self.app.languages, self)
        locale = locale or settings.i18n.default_locale

        if for_chameleon:
            return self.app.chameleon_translations.get(locale)
        else:
            return self.app.translations.get(locale)

    def message(self, text, type):
        """ Adds a message with the given type to the messages list. This
        messages list may then be displayed by an applicaiton building on
        onegov.core.

        For example:

            http://foundation.zurb.com/docs/components/alert_boxes.html

        Four default types are defined on the request for easier use:

        :meth:`success`
        :meth:`warning`
        :meth:`info`
        :meth:`alert`

        The messages are stored with the session and to display them, the
        template using the messages should call :meth:`consume_messages`.

        """
        if not self.browser_session.has('messages'):
            self.browser_session.messages = [Message(text, type)]
        else:
            # this is a bit akward, but I don't see an easy way for this atm.
            # (otoh, usually there's going to be one message only)
            self.browser_session.messages = self.browser_session.messages + [
                Message(text, type)
            ]

    def consume_messages(self):
        """ Returns the messages, removing them from the session in the
        process. Call only if you can be reasonably sure that the user
        will see the messages.

        """
        if self.browser_session.has('messages'):
            for message in self.browser_session.messages:
                yield message

            del self.browser_session.messages

    def success(self, text):
        """ Adds a success message. """
        self.message(text, 'success')

    def warning(self, text):
        """ Adds a warning message. """
        self.message(text, 'warning')

    def info(self, text):
        """ Adds an info message. """
        self.message(text, 'info')

    def alert(self, text):
        """ Adds an alert message. """
        self.message(text, 'alert')
