from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")
        new_equipment = self.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise ValueError("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        new_team = self.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self._find_last_equipment_by_type(equipment_type)
        team = self._find_team_by_name(team_name)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)
        if team is None:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_eq_pcs = len([eq.increase_price() for eq in self.equipment if eq.TYPE_ == equipment_type])
        return f"Successfully changed {changed_eq_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)
        if not team1.TYPE_ == team2.TYPE_:
            raise Exception(f"Game cannot start! Team types mismatch!")
        team1_points = team1.sum_points()
        team2_points = team2.sum_points()
        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."
        if team1_points < team2_points:
            team2.win()
            return f"The winner is {team2.name}."
        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

    # helper methods

    def _find_last_equipment_by_type(self, equipment_type):
        collection = [eq for eq in self.equipment if eq.TYPE_ == equipment_type]
        return collection[-1] if collection else None

    def _find_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None


# t = Tournament('SoftUniada2023', 2)
#
# print(t.add_equipment('KneePad'))
# print(t.add_equipment('ElbowPad'))
#
# print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
# print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
# print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))
#
# print(t.sell_equipment('KneePad', 'Spartak'))
#
# print(t.remove_team('Levski'))
# print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))
#
# print(t.increase_equipment_price('ElbowPad'))
# print(t.increase_equipment_price('KneePad'))
#
# print(t.play('Lokomotiv', 'Spartak'))
#
# print(t.get_statistics())
