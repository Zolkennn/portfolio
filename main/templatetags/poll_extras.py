from django import template

register = template.Library()

def split(str:  str, sep):
    """Removes all values of arg from the given string"""
    return str.split(sep)

register.filter("split", split)