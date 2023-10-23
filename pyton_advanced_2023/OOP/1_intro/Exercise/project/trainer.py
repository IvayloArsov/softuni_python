from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name=None):
        self.name = name
        self.pokemons = list()

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name not in [caught.name for caught in self.pokemons]:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.name} with health {pokemon.health}'
        return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        for pok in self.pokemons[:]:
            if pokemon_name == pok.name:
                self.pokemons.remove(pok)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        statement = []
        statement.append(f'Pokemon Trainer {self.name}')
        statement.append(f'Pokemon count {len(self.pokemons)}')
        for pokemon in self.pokemons:
            pokemon_details = f'- {pokemon.pokemon_details()}'
            statement.append(pokemon_details)

        return "\n".join(statement)


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
