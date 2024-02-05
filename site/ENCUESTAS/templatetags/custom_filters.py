from django import template

register = template.Library()

@register.simple_tag
def sum_numbers(initial_value, to_add):
    return initial_value + to_add
