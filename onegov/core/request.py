import collections

from cached_property import cached_property
from datetime import timedelta
from itsdangerous import (
    BadSignature,
    SignatureExpired,
    TimestampSigner
)
from more.webassets.core import IncludeRequest
from morepath.security import NO_IDENTITY
from onegov.core import compat
from onegov.core import utils
from onegov.core.crypto import random_token
from webob.exc import HTTPForbidden
from wtforms.csrf.session import SessionCSRF


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

    @cached_property
    def url(self):
        """ Returns the current url, taking the virtual hosting in account. """
        return self.transform(self.path)

    def transform(self, url):
        """ Applies X_VHM_HOST and X_VHM_ROOT to the given url (which is
        expected to not contain a host yet!). """
        if self.x_vhm_root:
            url = '/' + utils.lchop(url, self.x_vhm_root).lstrip('/')

        if self.x_vhm_host:
            url = self.x_vhm_host + url
        else:
            url = self.host_url + url

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
    def browser_session(self):
        """ Returns a browser_session bound to the request. Works via cookies,
        so requests without cookies won't be able to use the browser_session.

        The browser session is bound to the application (by id), so no session
        data is shared between the applications.

        If no data is written to the browser_session, no session_id cookie
        is created.

        """

        session_id = self.app.unsign(self.cookies.get('session_id', ''))

        if not session_id:
            session_id = random_token()

        def on_dirty(namespace, token):
            self.cookies['session_id'] = self.app.sign(token)

            @self.after
            def store_session(response):
                response.set_cookie(
                    'session_id',
                    self.cookies['session_id'],
                    secure=self.app.identity_secure,
                    httponly=True
                )

        return self.app.modules.browser_session.BrowserSession(
            namespace=self.app.application_id,
            token=session_id,
            cache=self.app.cache,
            on_dirty=on_dirty
        )

    def get_form(self, form_class,
                 i18n_support=True, csrf_support=True, data=None):
        """ Returns an instance of the given form class, set up with the
        correct translator and with CSRF protection enabled (the latter
        doesn't work yet).

        """
        meta = {}

        if i18n_support:
            translate = self.get_translate(for_chameleon=False)
            form_class = self.app.modules.i18n.get_translation_bound_form(
                form_class, translate)

            meta['locales'] = self.app.languages

        if csrf_support:
            meta['csrf'] = True,
            meta['csrf_context'] = self.browser_session
            meta['csrf_class'] = SessionCSRF
            meta['csrf_secret'] = self.app.csrf_secret.encode('utf-8')
            meta['csrf_time_limit'] = timedelta(
                seconds=self.app.csrf_time_limit)

        return form_class(self.POST, meta=meta, data=data)

    def translate(self, text):
        """ Transalates the given text, if it's a translatable text. """

        if not hasattr(text, 'domain'):
            return text

        return self.translator(text)

    @cached_property
    def translator(self):
        """ Returns the translate function for basic string translations. """
        translator = self.get_translate()

        if compat.PY3:
            return lambda text: text.interpolate(translator.gettext(text))
        else:
            return lambda text: text.interpolate(translator.ugettext(text))

    @cached_property
    def locale(self):
        """ Returns the current locale of this request. """
        settings = self.app.registry.settings

        locale = settings.i18n.locale_negotiator(self.app.languages, self)
        return locale or settings.i18n.default_locale

    def get_translate(self, for_chameleon=False):
        """ Returns the translate method to the given request, or None
        if no such method is availabe.

        :for_chameleon:
            True if the translate instance is used for chameleon (which is
            special).

        """
        if not self.app.languages:
            return None

        if for_chameleon:
            return self.app.chameleon_translations.get(self.locale)
        else:
            return self.app.translations.get(self.locale)

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

    @cached_property
    def is_logged_in(self):
        """ Returns True if the current request is logged in at all. """
        return self.identity is not NO_IDENTITY

    def has_permission(self, model, permission):
        """ Returns True if the current user has the given permission on the
        given model.

        """
        if self.is_logged_in:
            permitted = self.app.modules.rules.has_permission_logged_in
        else:
            permitted = self.app.modules.rules.has_permission_not_logged_in

        return permitted(self.identity, model, permission)

    def exclude_invisible(self, models):
        """ Excludes models invisble to the current user from the list. """
        return [m for m in models if self.is_visible(m)]

    def is_visible(self, model):
        """ Returns True if the given model is visible to the current user.
        This is basically an alias for :meth:`CoreRequest.is_public`. It exists
        because it is easier to understand than ``is_public``.

        """
        return self.has_permission(model, self.app.modules.security.Public)

    def is_public(self, model):
        """ Returns True if the current user has the Public permission for
        the given model.

        """
        return self.has_permission(model, self.app.modules.security.Public)

    def is_private(self, model):
        """ Returns True if the current user has the Private permission for
        the given model.

        """
        return self.has_permission(model, self.app.modules.security.Private)

    def is_secret(self, model):
        """ Returns True if the current user has the Secret permission for
        the given model.

        """
        return self.has_permission(model, self.app.modules.security.Secret)

    @cached_property
    def current_role(self):
        """ Returns the user-role of the current request, if logged in.
        Otherwise, None is returned.

        """
        return self.is_logged_in and self.identity.role or None

    @cached_property
    def csrf_salt(self):
        if not self.browser_session.has('csrf_salt'):
            self.browser_session['csrf_salt'] = random_token()

        return self.browser_session['csrf_salt']

    def new_csrf_token(self):
        """ Returns a new CSRF token. A CSRF token can be verified
        using :meth:`is_valid_csrf_token`.

        Note that forms do their own CSRF protection. This is meant
        for CSRF protection outside of forms.

        onegov.core uses the Synchronizer Token Pattern for CSRF protection:
        `<https://www.owasp.org/index.php/\
        Cross-Site_Request_Forgery_%28CSRF%29_Prevention_Cheat_Sheet>`_

        New CSRF tokens are signed usign a secret attached to the session (but
        not sent out to the user). Clients have to return the CSRF token they
        are given. The token has to match the secret, which the client doesn't
        know. So an attacker would have to get access to both the cookie and
        the html source to be able to forge a request.

        Since cookies are marked as HTTP only (no javascript access), this
        even prevents CSRF attack combined with XSS.

        """
        # no csrf tokens for anonymous users (there's not really a point
        # to doing this)
        if not self.is_logged_in:
            return ''

        # use app.identity_secret here, because that's being used for
        # more.itsdangerous, which uses the same algorithm
        assert self.csrf_salt

        signer = TimestampSigner(self.app.identity_secret, salt=self.csrf_salt)
        return signer.sign(random_token())

    def assert_valid_csrf_token(self, signed_value=None):
        """ Validates the given CSRF token and returns if it was
        created by :meth:`new_csrf_token`. If there's a mismatch, a 403 is
        raised.

        If no signed_value is passed, it is taken from
        request.params.get('csrf-token').

        """
        signed_value = signed_value or self.params.get('csrf-token')

        if not signed_value:
            raise HTTPForbidden()

        if not self.csrf_salt:
            raise HTTPForbidden()

        signer = TimestampSigner(self.app.identity_secret, salt=self.csrf_salt)
        try:
            signer.unsign(signed_value, max_age=self.app.csrf_time_limit)
        except (SignatureExpired, BadSignature):
            raise HTTPForbidden()
