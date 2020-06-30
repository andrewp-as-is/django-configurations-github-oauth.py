<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-configurations-github-oauth.svg?maxAge=3600)](https://pypi.org/project/django-configurations-github-oauth/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-configurations-github-oauth.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-configurations-github-oauth.py/actions)

### Installation
```bash
$ [sudo] pip install django-configurations-github-oauth
```

##### `settings.py`
```python
from django_configurations_github_oauth import GithubOAuthConfiguration

class Base(GithubOAuthConfiguration,...):
    pass
```

##### `.env`
```bash
DJANGO_GITHUB_OAUTH_CLIENT_ID=CLIENT_IDs
DJANGO_GITHUB_OAUTH_SECRET=OAUTH_SECRET
DJANGO_GITHUB_OAUTH_CALLBACK_URL=http://127.0.0.1:8000/
DJANGO_GITHUB_OAUTH_SCOPES=user,repo
```

#### Links
+   [django-configurations](https://github.com/jazzband/django-configurations)
+   [github.com/settings/developers](https://github.com/settings/developers)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>