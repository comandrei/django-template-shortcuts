from django import template
from template_shortcuts.providers import CDNJS
from template_shortcuts.nodes import CSSTag, JSTag

provider = CDNJS()


def parse_tag(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, version = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" %
            token.contents.split()[0])
    if not (version[0] == version[-1] and version[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name)
    return tag_name, version[1:-1]


def javascript_tag(parser, token):
    tag_name, version = parse_tag(parser, token)
    url_builder = getattr(provider, tag_name)
    if url_builder:
        url = url_builder(version)
        return JSTag(url)
    raise template.TemplateSyntaxError(
        "Unsupported library '%s'" % tag_name)

register = template.Library()
JS_TAGS = ["angular", "modernizr", "jquery"]
for tag in JS_TAGS:
    register.tag(tag, javascript_tag)
