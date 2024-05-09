from django import template

register = template.Library()

@register.filter(name='slice_range')
def slice_range(value, arg):
    """
    Slices the list or queryset up to the specified range.
    """
    return value[:int(arg)]