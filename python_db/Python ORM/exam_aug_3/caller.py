import os
import django
from django.db.models import Q, Count, F, Avg

from main_app.models import Astronaut, Mission, Spacecraft

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here

# Create queries within functions

def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    search_string = search_string.strip()

    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by('name')

    if not astronauts.exists():
        return ''

    result = []
    for astronaut in astronauts:
        status = 'Active' if astronaut.is_active else 'Inactive'
        result.append(f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {status}")

    return '\n'.join(result)


def get_top_astronaut():
    astronaut = (Astronaut.objects
                 .annotate(num_of_missions=Count('missions'))
                 .order_by('-num_of_missions', 'phone_number')
                 .first())
    if astronaut is None or astronaut.num_of_missions == 0:
        return 'No data.'
    return f"Top Astronaut: {astronaut.name} with {astronaut.num_of_missions} missions."


def get_top_commander():
    commander = (Astronaut.objects
                 .annotate(num_of_missions=Count('commander_mission'))
                 .order_by('-num_of_missions', 'phone_number')
                 .first())
    if commander is None or commander.num_of_missions == 0:
        return 'No data.'
    return f"Top Commander: {commander.name} with {commander.num_of_missions} commanded missions."


def get_last_completed_mission():
    mission = (Mission.objects
               .filter(status='Completed')
               .order_by('-launch_date')
               .select_related('commander', 'spacecraft')
               .prefetch_related('astronauts')
               .first())

    if not mission:
        return "No data."

    commander_name = mission.commander.name if mission.commander else "TBA"

    astronauts = mission.astronauts.order_by('name')
    astronaut_names = ", ".join(astronaut.name for astronaut in astronauts)

    total_spacewalks = sum(astronaut.spacewalks for astronaut in astronauts)

    return (f"The last completed mission is: {mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronaut_names}. "
            f"Spacecraft: {mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():
    if not Mission.objects.exists():
        return 'No data.'

    spacecraft = (Spacecraft.objects
                  .annotate(num_missions=Count('missions'))
                  .order_by('-num_missions', 'name')
                  .first())

    num_astronauts = (spacecraft.missions
                      .values('astronauts')
                      .distinct()
                      .count())

    return (f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.num_missions} missions, astronauts on missions: {num_astronauts}.")


def decrease_spacecrafts_weight():
    planned_missions_filter = Q(status='Planned')
    weight_filter = Q(weight__gte=200.0)
    planned_missions = Mission.objects.filter(planned_missions_filter)
    spacecrafts_to_decrease = Spacecraft.objects.filter(
        missions__in=planned_missions
    ).distinct().filter(weight_filter)

    num_of_spacecrafts_affected = spacecrafts_to_decrease.count()

    if num_of_spacecrafts_affected == 0:
        return "No changes in weight."

    ids_to_update = spacecrafts_to_decrease.values_list('id', flat=True)
    Spacecraft.objects.filter(id__in=ids_to_update).update(weight=F('weight') - 200.0)

    Spacecraft.objects.filter(weight__lt=0.0).update(weight=0.0)

    avg_weight = Spacecraft.objects.aggregate(Avg('weight'))['weight__avg']
    avg_weight = round(avg_weight, 1)

    return (f"The weight of {num_of_spacecrafts_affected} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight}kg")