from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply
from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def find_object_by_attribute_value_in_list(lst: list, attribute: str, value: str):
        return next((item for item in lst if getattr(item, attribute, None) == value), None)

    def add_player(self, *players: Player):
        temp_lst = [player for player in players if player not in self.players]
        self.players = list(set(self.players).union(temp_lst))
        return f"Successfully added: {', '.join([player.name for player in temp_lst])}"

    def add_supply(self, *supplies: Food or Drink):
        temp_list = [supply for supply in supplies]
        self.supplies = list(set(self.supplies).union(temp_list))

    def sustain(self, player_name: str, sustenance_type: str):
        item = [
            item for item in self.supplies
            if item.type_ == sustenance_type
        ][-1]

