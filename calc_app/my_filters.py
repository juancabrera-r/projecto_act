from django.template.defaultfilters import register


@register.filter(name='times')
def times(number):
    return range(number)