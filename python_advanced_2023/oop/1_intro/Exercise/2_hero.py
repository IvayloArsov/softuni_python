class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'

    def heal(self, amount: int):
        if self.health > 0:
            self.health += amount


hero = Hero("Alexander", 75)
print(hero.defend(20))
print(hero.defend(100))
print(hero.heal(20))
