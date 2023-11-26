from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    musicians_dict = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }
    drummer_skills = {
        'Rock': 'play the drums with drumsticks',
        'Metal': 'play the drums with drumsticks',
        'Jazz': 'play the drums with drum brushes'
    }
    singer_skills = {
        'Rock': 'sing high pitch notes',
        'Metal': 'sing low pitch notes',
        'Jazz': ['sing high pitch notes', 'sing low pitch notes']
    }
    guitarist_skills = {
        'Rock': 'play rock',
        'Metal': 'play metal',
        'Jazz': 'play jazz'
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.musicians_dict.keys():
            raise ValueError("Invalid musician type!")
        new_musician = self.find_obj_by_name(name, self.musicians)
        if new_musician:
            raise Exception(f"{new_musician.name} is already a musician!")
        new_musician = self.musicians_dict[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        new_band = self.find_obj_by_name(name, self.bands)
        if new_band:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_obj_by_name(musician_name, self.musicians)
        band = self.find_obj_by_name(band_name, self.bands)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_obj_by_name(band_name, self.bands)
        musician = self.find_obj_by_name(musician_name, band.members)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_obj_by_name(band_name, self.bands)
        members = set(member.__class__.__name__ for member in band.members)
        if len(members) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [concert for concert in self.concerts if concert.place == concert_place][0]
        for member in band.members:
            if isinstance(member, Drummer) and self.drummer_skills[concert.genre] not in member.skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif isinstance(member, Singer) and self.singer_skills[concert.genre] not in member.skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif isinstance(member, Guitarist) and self.guitarist_skills[concert.genre] not in member.skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = (concert.ticket_price * concert.audience) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    #  Helper function to find objects by their name in the given class sublist
    @staticmethod
    def find_obj_by_name(obj_name, obj_list):
        obj = [obj for obj in obj_list if obj.name == obj_name]
        return obj[0] if obj else None
