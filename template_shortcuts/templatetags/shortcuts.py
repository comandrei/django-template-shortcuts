from django import template

from template_shortcuts.utils import setting, import_by_path
from template_shortcuts.nodes import CSSTag, JSTag

provider = import_by_path(setting("TEMPLATE_CDN_PROVIDER"))()


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


def css_tag(parser, token):
    tag_name, version = parse_tag(parser, token)
    url_builder = getattr(provider, tag_name)
    if url_builder:
        url = url_builder(version)
        return CSSTag(url)
    raise template.TemplateSyntaxError(
        "Unsupported library '%s'" % tag_name)

register = template.Library()
JS_TAGS = ["angular", "chrome_frame", "dojo", "ext_core",
           "jquery", "jquery_ui", "mootools", "modernizr",
           "prototype", "scriptaculos", "webfont"]

for tag in JS_TAGS:
    register.tag(tag, javascript_tag)
