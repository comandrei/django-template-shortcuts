django-template-shorcuts
========================

.. image:: https://travis-ci.org/comandrei/django-template-shortcuts.svg
    :target: https://travis-ci.org/comandrei/django-template-shortcuts
    :alt: CI

.. image:: https://img.shields.io/pypi/v/django-template-shortcuts.svg
    :target: https://pypi.python.org/pypi/django-template-shortcuts
    :alt: Version

.. image:: https://img.shields.io/pypi/dm/django-template-shortcuts.svg
    :target: https://pypi.python.org/pypi/django-template-shorcuts
    :alt: Downloads


Remove boilerplate code when including JS and CSS files hosted by popular CDNs.

Requirements
============

Core
----

* Python 2.7+ or Python 3.3+
* Django 1.7 through Django 1.9


Installation
============

.. code:: bash

          pip install django-template-shorcuts

Add to your installed apps in settings

.. code:: python

          INSTALLED_APPS = (
          ...
          'template_shortcuts',
          ...
          )
	  TEMPLATE_CDN_PROVIDER = "template_shortcuts.providers.google.Google"


There is support for multiple CDN backends and multiple JS libraries.
Currently only the Google CDN is supported with some support for Cloudfare's CDNJS.

Usage
=====

.. code:: python

          {% load shortcuts %}
	  {% jquery "1.7.2" %}

Will yeild:

.. code:: html

          <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>


Contributing
============
  Found an issue or just want to add some functionality? Open an issue in the issue tracker on github, fork the project, hack away, and make a pull request when you're done.
