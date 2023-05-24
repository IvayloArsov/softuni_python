pokemons_nearby = [int(num) for num in input().split(" ")]
poke_value = 0

while len(pokemons_nearby) > 0:

    caught_pokemon = int(input())
    
    if caught_pokemon < 0:
        caught_pokemon = max(caught_pokemon, 0)
        value_caught = pokemons_nearby.pop(caught_pokemon)
        pokemons_nearby.insert(0, pokemons_nearby[-1])

    elif caught_pokemon >= len(pokemons_nearby):
        caught_pokemon = min(caught_pokemon, len(pokemons_nearby) - 1)
        value_caught = pokemons_nearby.pop(caught_pokemon)
        pokemons_nearby.append(pokemons_nearby[0])
    else:
        value_caught = pokemons_nearby.pop(caught_pokemon)

    poke_value += value_caught

    for i in range(len(pokemons_nearby)):
        if value_caught >= pokemons_nearby[i]:
            pokemons_nearby[i] += value_caught
        else:
            pokemons_nearby[i] -= value_caught


print(poke_value)