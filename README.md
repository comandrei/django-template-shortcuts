django-template-shortcuts
=========================

[![Build Status](https://travis-ci.org/comandrei/django-template-shortcuts.png)](https://travis-ci.org/comandrei/django-template-shortcuts)

Reusable Django templatetags





## Index

- [Instalation](#instalation)
- [Contributing](#contributing)
- [Usage](#usage)
 - [Tags](#tags)
 - [Filters](#filters)

## Instalation

Via pip:
```bash
    pip install django-template-utils
```
Via easy_install:
```bash
    easy_install django-template-utils
```
Clonning the project:
```bash
    $ git clone git://github.com/gerardo-orozco/django-template-utils.git
    $ python django-template-utils/setup.py install
```

Add the app to your istalled apps:
```python
    INSTALLED_APPS = (
        ...
        'template_shortcuts',
        ...
    )
	TEMPLATE_CDN_PROVIDER = "template_shortcuts.provides.google.Google"
```
