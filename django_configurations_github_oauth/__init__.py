import os

from configurations import Configuration, values

APP = 'django_github_oauth'
AUTH_USER_MODEL = 'django_github_oauth.User'
AUTHENTICATION_BACKEND = 'django_passwordless_auth.backend.PasswordlessAuthBackend'

class GithubOAuthConfiguration(Configuration):
    GITHUB_OAUTH_CLIENT_ID = values.Value(None)
    GITHUB_OAUTH_SECRET = values.Value(None)
    GITHUB_OAUTH_CALLBACK_URL = values.Value(None)
    GITHUB_OAUTH_SCOPES = values.ListValue([])

    @classmethod
    def pre_setup(cls):
        super(GithubOAuthConfiguration, cls).pre_setup()
        cls.AUTH_USER_MODEL = AUTH_USER_MODEL

    @classmethod
    def setup(cls):
        super(GithubOAuthConfiguration, cls).setup()
        if APP not in cls.INSTALLED_APPS:
            cls.INSTALLED_APPS.append(APP)
        if AUTHENTICATION_BACKEND not in cls.AUTHENTICATION_BACKENDS:
            cls.AUTHENTICATION_BACKENDS.append(AUTHENTICATION_BACKEND)

"""
        print('cls.AUTHENTICATION_BACKENDS = %s' % cls.AUTHENTICATION_BACKENDS)
        print('cls.AUTHENTICATION_BACKENDS.__class__ = %s' % cls.AUTHENTICATION_BACKENDS.__class__)
        print('cls.AUTHENTICATION_BACKENDS = list(%s)' % list(cls.AUTHENTICATION_BACKENDS))

"""
