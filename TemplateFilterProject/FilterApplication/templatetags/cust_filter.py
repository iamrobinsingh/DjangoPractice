from django import template

register = template.Library()

def truncate(value):
    result = value[0:5]
    return result
register.filter('truncate', truncate)

@register.filter(name ="truncate_n") # you can do by this type also
def truncate_n(value,n):
    result = value[0:n]
    return result
