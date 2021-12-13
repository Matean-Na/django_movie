from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.simple_tag()
def get_movies_count():
    """Количество фильмов"""
    movie = Movie.objects.all()
    return movie.count()


@register.simple_tag()
def get_actor_count():
    """Количество актеров"""
    actor = Actor.objects.all()
    return actor.count()


@register.simple_tag()
def get_review_count():
    """Количество отзывов"""
    reviews = Reviews.objects.all()
    return reviews.count()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=9):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}
