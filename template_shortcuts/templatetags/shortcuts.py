from django import template

register = template.Library()

class CSSTag(template.Node):

    def __init__(self, url):
        self.url = url

    def render(self, context):
        return '<link href="%s" type="text/css" rel="stylesheet" />' % self.url


class JSTag(template.Node):
    def __init__(self, url):
        self.url = url

    def render(self, context):
        return '<script type="text/javascript" src="%s"></script>' % self.url


@register.tag("jquery")
def jquery(parser, token):
    return JSTag("jquery.min.js")
