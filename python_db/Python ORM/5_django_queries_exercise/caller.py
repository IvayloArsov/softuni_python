import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from django.db.models import Q, When, Case, Value


# Create and check models
# Run and print your queries

### ArtGallery
def show_highest_rated_art():
    highest_rated = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f'{highest_rated.art_name} is the highest-rated art with a {highest_rated.rating} rating!'


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.all().filter(rating__lt=0).delete()


### Laptop

def show_the_most_expensive_laptop():
    priciest_laptop = Laptop.objects.all().order_by('-price', '-id').first()
    return f'{priciest_laptop.brand} is the most expensive laptop available for {priciest_laptop.price}$!'


def bulk_create_laptops(args):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand='Asus').update(operation_system='Windows')
    Laptop.objects.filter(brand='Apple').update(operation_system='MacOS')
    Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='Linux')
    Laptop.objects.filter(brand='Lenovo').update(operation_system='Chrome OS')


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


### Chess Player

def bulk_create_chess_players(*args):
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players():
    ChessPlayer.objects.filter(title__iexact='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title__iexact='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title__iexact='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM():
    (ChessPlayer.objects.all()
     .filter(rating__gte=2400)
     .update(title='GM'))


def grand_chess_title_IM():
    (ChessPlayer.objects.all()
     .filter(rating__gte=2300, rating__lte=2399)
     .update(title='IM'))


def grand_chess_title_FM():
    (ChessPlayer.objects.all()
     .filter(rating__gte=2200, rating__lte=2299)
     .update(title='FM'))


def grand_chess_title_regular_player():
    (ChessPlayer.objects.all()
     .filter(rating__gte=0, rating__lte=2199)
     .update(title='regular player'))
