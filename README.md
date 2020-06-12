<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/v/django-github-oauth-configuration.svg?maxAge=3600)](https://pypi.org/project/django-github-oauth-configuration/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-configurations-github-oauth.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-configurations-github-oauth.py/)

#### Installation
```bash
$ [sudo] pip install django-github-oauth-configuration
```

##### `settings.py`
```python
from django_configurations_github_oauth import GithubOAuthConfiguration

class Base(GithubOAuthConfiguration,...):
    pass
```

##### `.env`
```bash
GITHUB_OAUTH_CLIENT_ID=CLIENT_ID
GITHUB_OAUTH_SECRET=OAUTH_SECRET
GITHUB_OAUTH_CALLBACK_URL=http://127.0.0.1:8000/github-oauth/callback
GITHUB_OAUTH_SCOPES=user # optional
```

#### Links
+   [django-configurations](https://github.com/jazzband/django-configurations)
+   [github.com/settings/developers](https://github.com/settings/developers)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>