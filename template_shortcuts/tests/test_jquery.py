import unittest

from django import template

from template_shortcuts.tests.helpers import render_to_string


class JQueryTest(unittest.TestCase):

    def test_jquery_version_required(self):
        with self.assertRaises(template.TemplateSyntaxError):
            render_to_string("{% jquery %}")

    def test_jquery_certain_version(self):
        rendered = render_to_string("{% jquery '1.7.2' %}")
        self.assertIn("1.7.2/jquery.min.js", rendered)
