from django.test import TestCase
from django import template

from .helpers import render_to_string


class JQueryTest(TestCase):

    def test_jquery_version_required(self):
        with self.assertRaises(template.TemplateSyntaxError):
            render_to_string("{% jquery %}")

    def test_jquery_certain_version(self):
        rendered = render_to_string("{% jquery '1.7.2' %}")
        self.assertIn("1.7.2/jquery.min.js", rendered)


class AngularTestCase(TestCase):

    def test_angular_certain_version(self):
        rendered = render_to_string("{% angular '1.2.5' %}")
        self.assertIn("1.2.5/angular.min.js", rendered)
