from django import template

register = template.Library()


@register.filter(name='get_rating_user')
def get_rating_user(list, index):
    rating = list[index]
    if rating:
        return rating.rating
    else:
        return None


@register.filter(name="get_rating_id")
def get_rating_id(list, index):
    rating = list[index]
    if rating:
        return rating.id
    else:
        return None
