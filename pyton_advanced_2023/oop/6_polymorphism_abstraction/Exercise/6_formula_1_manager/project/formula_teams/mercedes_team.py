from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        self.budget = budget
        self.sponsors = {
            1: 1100000,
            2: 600000,
            3: 600000,
            4: 100000,
            5: 100000,
            6: 50000,
            7: 50000
        }
        self.expenses = 200000
