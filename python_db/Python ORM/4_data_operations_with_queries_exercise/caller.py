import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car


# Create queries within functions
def create_pet(name: str, species: str) -> str:
    pet = Pet(name=name, species=species)
    pet.save()
    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    artifact.save()
    return f'The artifact {name} is {age} years old!'


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.age > 250 and artifact.is_magical == True:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def create_location(name, region, population, description):
    location = Location(name=name, region=region, population=population, description=description)
    location.save()
    return


def show_all_locations():
    locations = Location.objects.all()
    line = [
        f'{location.name} has a population of {location.population}!'
        for location
        in sorted(locations, key=lambda x: -x.id)
    ]
    return '\n'.join(line)


def new_capital():
    capital = Location.objects.get(id=1)
    capital.is_capital = True
    capital.save()


def get_capitals():
    locations = Location.objects.all()
    capitals = locations.filter(is_capital=True)
    return capitals.values('name')


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        sum_of_digits = sum(int(digit) for digit in str(car.year))
        discounted_price = float(car.price) * (1 - sum_of_digits / 100)
        car.price_with_discount = discounted_price
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.all().last().delete()
