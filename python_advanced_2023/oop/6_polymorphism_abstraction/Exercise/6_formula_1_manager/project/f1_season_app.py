from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in ['Red Bull', 'Mercedes']:
            raise ValueError('Invalid team name!')
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)
        info_str = f'{team_name} has joined the new F1 season.'
        return info_str

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception('Not all teams have registered for the season.')
        info_str = f'Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. '
        info_str += f'Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. '
        first_team = 'Mercedes'
        if mercedes_pos > red_bull_pos:
            first_team = 'Red Bull'
        info_str += f'{first_team} is ahead at the {race_name} race.'
        return info_str


# f1_season = F1SeasonApp()
#
# print(f1_season.register_team_for_season("Red Bull", 2000000))
# print(f1_season.register_team_for_season("Mercedes", 2500000))
# print(f1_season.new_race_results("Nurburgring", 1, 7))
# print(f1_season.new_race_results("Silverstone", 10, 1))