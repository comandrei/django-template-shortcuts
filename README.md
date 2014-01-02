django-template-shortcuts
=========================

[![Build Status](https://travis-ci.org/comandrei/django-template-shortcuts.png)](https://travis-ci.org/comandrei/django-template-shortcuts)

Remove boilerplate code when including JS and CSS files hosted by popular CDNs.


## Index

- [Instalation and configuration](#instalation)
- [Usage](#usage)
- [Supported libraries](#support)

## Instalation

Via pip:
```bash
    pip install django-template-shortcuts
```
Via easy_install:
```bash
    easy_install django-template-shortcuts
```
Clonning the project:
```bash
    $ git clone git://github.com/comandrei/django-template-shortcuts.git
    $ python django-template-shortcuts/setup.py install
```

Add the app to your installed apps:
```python
    INSTALLED_APPS = (
        ...
        'template_shortcuts',
        ...
    )
	TEMPLATE_CDN_PROVIDER = "template_shortcuts.providers.google.Google"
```

There is support for multiple CDN backends and multiple JS libraries.
Currently only the Google CDN is supported with some support for Cloudfare's CDNJS.

## Usage

```python
	{% load shortcuts %}
	{% jquery "1.7.2" %}
```
Will yeild

```html
	<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
```

## Supported libraries

|Template Tag | Google | CDNJS |
|-------------|:-------:|:-------:|
|angular|:white_check_mark:|:white_check_mark:|
|chrome_frame|:white_check_mark:|:white_check_mark:|
|dojo|:white_check_mark:|:white_check_mark:|
|ext_core|:white_check_mark:|:white_check_mark:|
|jquery|:white_check_mark:|:white_check_mark:|
|jquery_ui|:white_check_mark:|:white_check_mark:|
|mootools|:white_check_mark:|:white_check_mark:|
|modernizr|:x:|:white_check_mark:|
|prototype|:white_check_mark:|:white_check_mark:|
|scriptaculos|:white_check_mark:|:white_check_mark:|
|webfont|:white_check_mark:|:white_check_mark:|


## Contributing
  Found an issue or just want to add some functionality? Open an issue in the issue tracker on github, fork the project, hack away, and make a pull request when you're done.
  
