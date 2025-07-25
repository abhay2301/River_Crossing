from django import template

register = template.Library()

@register.filter
def item_icon(item):
    icons = {
        'farmer': '👨‍🌾',
        'goat': '🐐',
        'wolf': '🐺',
        'cabbage': '🥬'
    }
    return icons.get(item, '')