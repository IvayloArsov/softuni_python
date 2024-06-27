import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


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
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    last_car = Car.objects.all().last()
    if last_car:
        last_car.delete()


def show_unfinished_task():
    tasks = Task.objects.filter(is_finished=False)
    unfinished_tasks = [
        f'Task - {task.title} needs to be done until {task.due_date}!'
        for task in tasks
    ]
    return '\n'.join(unfinished_tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    encoded_text = "".join([chr(ord(char) - 3) for char in text])
    Task.objects.filter(title=task_title).update(description=encoded_text)


def get_deluxe_rooms():
    rooms = HotelRoom.objects.all().filter(room_type='Deluxe')
    selected_deluxe_rooms = [
        f'Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!'
        for room in rooms
        if room.id % 2 == 0
    ]
    return '\n'.join(selected_deluxe_rooms)


def increase_room_capacity():
    reserved_rooms = HotelRoom.objects.all().filter(is_reserved=True).order_by('id')
    previous_capacity = None
    for room in reserved_rooms:
        if previous_capacity is not None:
            room.capacity += previous_capacity

        else:
            room.capacity += room.id

        room.save()
        previous_capacity = room.capacity


def reserve_first_room():
    first_room = HotelRoom.objects.get(id=1)
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if not last_room.is_reserved:
        last_room.delete()


def update_characters():
    characters = Character.objects.all()
    for character in characters:
        if character.class_name == Character.ClassType.MAGE:
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == Character.ClassType.WARRIOR:
            character.hit_points = character.hit_points // 2
            character.dexterity += 4
        elif character.class_name in [Character.ClassType.ASSASSIN, Character.ClassType.SCOUT]:
            character.inventory = "The inventory is empty"

        character.save()


def fuse_characters(first_character: Character, second_character: Character):
    new_name = f'{first_character.name} {second_character.name}'
    new_class_name = 'Fusion'
    new_level = (first_character.level + second_character.level) // 2
    new_strength = int((first_character.strength + second_character.strength) * 1.2)
    new_dexterity = int((first_character.dexterity + second_character.dexterity) * 1.4)
    new_intelligence = int((first_character.intelligence + second_character.intelligence) * 1.5)
    new_hit_points = first_character.hit_points + second_character.hit_points

    if first_character.class_name in (Character.ClassType.MAGE, Character.ClassType.SCOUT):
        new_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif first_character.class_name in [Character.ClassType.WARRIOR, Character.ClassType.ASSASSIN]:
        new_inventory = "Dragon Scale Armor, Excalibur"
    else:
        new_inventory = ""

    Character.objects.create(
        name=new_name,
        class_name=new_class_name,
        level=new_level,
        strength=new_strength,
        dexterity=new_dexterity,
        intelligence=new_intelligence,
        hit_points=new_hit_points,
        inventory=new_inventory
    )
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()
