from django import template
from ..models import Review

register = template.Library()

# Создаем свой тег шалона reviews.html
# Выводим все отзывы
@register.inclusion_tag('main/components/reviews.html')
def show_all_reviews():
    reviews = Review.objects.all()
    return {'reviews': reviews}