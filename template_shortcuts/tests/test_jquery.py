import unittest

from template_shortcuts.tests.helpers import render_to_string


class JQueryTest(unittest.TestCase):

    def test_jquery_latest(self):
        rendered = render_to_string("{% jquery %}")
        self.assertIn("jquery.min.js", rendered)

    def test_jquery_certain_version(self):
        pass
