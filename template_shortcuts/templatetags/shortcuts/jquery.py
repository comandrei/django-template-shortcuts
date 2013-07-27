from nodes import JSTag

def jquery(parser, token):
    return JSTag("jquery.min.js")
