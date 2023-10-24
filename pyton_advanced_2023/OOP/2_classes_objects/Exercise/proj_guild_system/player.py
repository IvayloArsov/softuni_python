class Player:
    def __init__(self, name:str, hp:int, mp:int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = dict()
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return f"Skill already added"

        self.skills[skill_name] = int(mana_cost)
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = [
            f'Name: {self.name}',
            f'Guild: {self.guild}',
            f'HP: {self.hp}',
            f'MP: {self.mp}'
        ]
        for skill, mc in self.skills.items():
            result.append(f'==={skill} - {mc}')

        return '\n'.join(result)
