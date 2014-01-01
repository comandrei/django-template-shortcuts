from django import template
from nodes import JSTag


class JQueryTag(JSTag):
    base_url = "//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"

    def __init__(self, version):
        self.url = self.base_url % version


def jquery(parser, token):
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
    return JQueryTag(version=version[1:-1])
