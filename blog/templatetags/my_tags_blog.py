from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.filter()
def truncatechars(path):
    if len(path) >= 100:
        return path[0:99]
    return path
