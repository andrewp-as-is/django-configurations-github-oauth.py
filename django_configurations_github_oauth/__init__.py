import os

from configurations import Configuration, values

APP = 'django_github_oauth'
AUTHENTICATION_BACKEND = 'django_passwordless_auth.backend.PasswordlessAuthBackend'


class GithubOAuthConfiguration(Configuration):
    GITHUB_OAUTH_CLIENT_ID = values.Value(None)
    GITHUB_OAUTH_SECRET = values.Value(None)
    GITHUB_OAUTH_CALLBACK_URL = values.Value(None)
    GITHUB_OAUTH_SCOPES = values.ListValue([])
    LOGIN_URL = '/github-oauth/login'

    @classmethod
    def setup(cls):
        super(GithubOAuthConfiguration, cls).setup()
        if APP not in cls.INSTALLED_APPS:
            cls.INSTALLED_APPS.append(APP)
        if AUTHENTICATION_BACKEND not in cls.AUTHENTICATION_BACKENDS:
            cls.AUTHENTICATION_BACKENDS.append(AUTHENTICATION_BACKEND)
