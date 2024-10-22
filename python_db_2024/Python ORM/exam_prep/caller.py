import os
from datetime import date
from decimal import Decimal

import django
from django.db.models import Q, Count, Avg, F

from main_app.models import Director, Actor, Movie

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here

# Create queries within functions
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    directors = []
    if search_name is None:
        directors = Director.objects.filter(
            nationality__icontains=search_nationality
        ).order_by('full_name')

    elif search_nationality is None:
        directors = Director.objects.filter(
            full_name__icontains=search_name
        ).order_by('full_name')
    else:
        directors = Director.objects.filter(
            full_name__icontains=search_name,
            nationality__icontains=search_nationality
        ).order_by('full_name')

    if not directors:
        return ''
    result = [
        f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}"
        for director in directors
    ]

    return '\n'.join(result)


def get_top_director():
    directors = Director.objects.get_directors_by_movies_count()
    top_director = directors.first()
    if not top_director:
        return ''
    result = f"Top Director: {top_director.full_name}, movies: {top_director.movie_count}."
    return result


def get_top_actor():
    top_actor = Actor.objects.annotate(
        total_starring_movies=Count('actor_starring_movies'),
        movies_avg_rating=Avg('actor_starring_movies__rating')
    ).order_by('-total_starring_movies', 'full_name').first()

    if not Movie.objects.all() or not top_actor:
        return ""

    top_actor_movies = ', '.join([m.title for m in top_actor.actor_starring_movies.all()])

    return f"Top Actor: {top_actor.full_name}, starring in movies: {top_actor_movies}, " \
           f"movies average rating: {top_actor.movies_avg_rating:.1f}"


def get_actors_by_movies_count():
    top_actors = Actor.objects.annotate(
        total_movies=Count('actor_all_movies')
    ).order_by('-total_movies', 'full_name')[:3]
    if not top_actors or not Movie.objects.all():
        return ''
    result = [
        f'{actor.full_name}, participated in {actor.total_movies} movies'
        for actor in top_actors
    ]
    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_rated_movie = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()
    if not top_rated_movie:
        return ''

    starring_actor = top_rated_movie.starring_actor.full_name if top_rated_movie.starring_actor else 'N/A'

    participating_actors = ', '.join([
        actor.full_name
        for actor in top_rated_movie.actors.order_by('full_name')
    ])

    return (f'Top rated awarded movie: {top_rated_movie.title}, '
            f'rating: {float(top_rated_movie.rating):.1f}. '
            f'Starring actor: {starring_actor}. Cast: {participating_actors}.')


def increase_rating():
    classics = Movie.objects.filter(is_classic=True, rating__lt=10.0)
    if not classics.exists():
        return f'No ratings increased.'

    classics_updated = classics.update(rating=F('rating') + 0.1)

    return f"Rating increased for {classics_updated} movies."