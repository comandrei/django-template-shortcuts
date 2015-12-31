from django.template import Template, Context

def render_to_string(string, context=None):
    base_str = "{% load shortcuts %}"
    template_str = base_str + string
    if context is None:
        context = {}
    template = Template(template_str)
    return template.render(Context(context))
