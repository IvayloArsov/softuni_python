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


### Meal
def set_new_chefs():
    Meal.objects.update(
        chef=Case(
            When(meal_type='Breakfast', then=Value('Gordon Ramsay')),
            When(meal_type='Lunch', then=Value('Julia Child')),
            When(meal_type='Dinner', then=Value('Jamie Oliver')),
            When(meal_type='Snack', then=Value('Thomas Keller'))
        )
    )


def set_new_preparation_times():
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type='Breakfast', then=Value('10 minutes')),
            When(meal_type='Lunch', then=Value('12 minutes')),
            When(meal_type='Dinner', then=Value('15 minutes')),
            When(meal_type='Snack', then=Value('5 minutes')),
        )
    )


def update_low_calorie_meals():
    (Meal.objects.all()
     .filter(meal_type__in=['Breakfast', 'Dinner'])
     .update(calories=400))


def update_high_calorie_meals():
    (Meal.objects.all()
     .filter(meal_type__in=['Lunch', 'Snack'])
     .update(calories=700))


def delete_lunch_and_snack_meals():
    (Meal.objects.all()
     .filter(meal_type__in=['Lunch', 'Snack'])
     .delete())


### Dungeon

def show_hard_dungeons():
    dungeons = (Dungeon.objects.all()
                .filter(difficulty='Hard')
                .order_by('-location'))
    dungeons = [
        f'{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!'
        for dungeon in dungeons
    ]
    return '\n'.join(dungeons)


def bulk_create_dungeons(*args):
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names():
    Dungeon.objects.all().update(
        name=Case(
            When(difficulty='Easy', then=Value('The Erased Thombs')),
            When(difficulty='Medium', then=Value("The Coral Labyrinth")),
            When(difficulty='Hard', then=Value("The Lost Haunt"))
        )
    )


def update_dungeon_bosses_health():
    (Dungeon.objects.all()
     .exclude(difficulty='Easy')
     .update(boss_health=500))


def update_dungeon_recommended_levels():
    Dungeon.objects.all().update(
        recommended_level=Case(
            When(difficulty='Easy', then=Value(25)),
            When(difficulty='Medium', then=Value(50)),
            When(difficulty='Hard', then=Value(75)),
        )
    )


def update_dungeon_rewards():
    Dungeon.objects.all().update(
        reward=Case(
            When(boss_health=500, then=Value('1000 Gold')),
            When(location__startswith='E', then=Value('New dungeon unlocked')),
            When(location__endswith='s', then=Value('Dragonheart Amulet'))
        )
    )


def set_new_locations():
    Dungeon.objects.all().update(
        location=Case(
            When(recommended_level=25, then=Value('Enchanted Maze')),
            When(recommended_level=50, then=Value('Grimstone Mines')),
            When(recommended_level=75, then=Value('Shadowed Abyss')),
        )
    )


### Workout

def show_workouts():
    filtered_workouts = (Workout.objects.all()
                         .filter(workout_type__in=['Calisthenics', 'CrossFit']))
    workouts = [
        f'{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!'
        for workout in filtered_workouts
    ]
    return '\n'.join(workouts)


def get_high_difficulty_cardio_workouts():
    return (Workout.objects
            .filter(Q(workout_type='Cardio') & Q(difficulty='High'))
            .order_by('instructor'))


def set_new_instructors():
    Workout.objects.all().update(
        instructor=Case(
            When(workout_type='Cardio', then=Value('John Smith')),
            When(workout_type='Strength', then=Value('Michael Williams')),
            When(workout_type='Yoga', then=Value('Emily Johnson')),
            When(workout_type='CrossFit', then=Value('Sarah Davis')),
            When(workout_type='Calisthenics', then=Value('Chris Heria')),
        )
    )


def set_new_duration_times():
    Workout.objects.all().update(
        duration=Case(
            When(instructor='John Smith', then=Value('15 minutes')),
            When(instructor='Sarah Davis', then=Value('30 minutes')),
            When(instructor='Chris Heria', then=Value('45 minutes')),
            When(instructor='Michael Williams', then=Value('1 hour')),
            When(instructor='Emily Johnson', then=Value('1 hour and 30 minutes'))
        )
    )


def delete_workouts():
    (Workout.objects.all()
     .exclude(workout_type__in=['Strength', 'Calisthenics'])
     .delete())