from django import template

register = template.Library()

class UppercaseNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

@register.tag(name="uppercase")
def do_uppercase(parser, token):
    nodelist=parser.parse(('enduppercase',))
    parser.delete_first_token()
    return UppercaseNode(nodelist)

