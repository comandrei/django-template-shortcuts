import collections

import mock

from django.template import Template, Context

SETTINGS = collections.namedtuple(
    "Settings", ["TEMPLATE_DEBUG", "INSTALLED_APPS"])
settings = SETTINGS(False, ["template_shortcuts"])

@mock.patch("django.template.base.settings", settings)
def render_to_string(string, context=None):
    base_str = "{% load shortcuts %}"
    template_str = base_str + string
    if context is None:
        context = {}
    template = Template(template_str)
    return template.render(Context(context))
