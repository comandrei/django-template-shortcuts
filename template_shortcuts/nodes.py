from django import template


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
