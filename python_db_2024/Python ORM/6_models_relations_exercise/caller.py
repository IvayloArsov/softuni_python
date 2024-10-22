import os
from datetime import timedelta, date

import django
from django.db.models import Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import *


# Create queries within functions
# Library
def show_all_authors_with_their_books():
    authors = Author.objects.all()
    result = []
    for author in authors:
        books = author.books.all()
        if books.exists():
            book_titles = ', '.join([book.title for book in books])
            result.append(f'{author.name} has written - {book_titles}!')
    return '\n'.join(result)


def delete_all_authors_without_books():
    authors = Author.objects.exclude(books__isnull=False)
    authors.delete()


# Music App
def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)
    artist.save()


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)
    artist.save()


# Shop
def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    average_rating_score = product.reviews.aggregate(Avg('rating'))['rating__avg']
    return average_rating_score


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.all().filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.all().filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    products = Product.objects.all().filter(reviews__isnull=True)
    products.delete()


# License

def calculate_licenses_expiration_dates():
    licences = DrivingLicense.objects.all()
    result = []
    for l in licences:
        exp_date = l.issue_date + timedelta(days=365)
        result.append(f'License with number: {l.license_number} expires on {exp_date}!')

    return '\n'.join(sorted(result, reverse=True))


def get_drivers_with_expired_licenses(due_date: date):
    licenses = DrivingLicense.objects.all()

    result = []
    for l in licenses:
        expiration_date = l.issue_date + timedelta(days=365)

        if expiration_date > due_date:
            result.append(l.driver)
    return result


# Car Registration
def register_car_by_owner(owner: Owner):
    free_registration = Registration.objects.all().filter(car__isnull=True).first()
    free_car = Car.objects.all().filter(owner__isnull=True).first()
    registration_date = date.today()
    free_registration.car = free_car
    free_registration.registration_date = registration_date
    free_registration.save()

    free_car.owner = owner
    free_car.save()

    car_model = free_car.model
    owner_name = free_car.owner.name
    reg_number = free_registration.registration_number

    return f"Successfully registered {car_model} to {owner_name} with registration number {reg_number}."


