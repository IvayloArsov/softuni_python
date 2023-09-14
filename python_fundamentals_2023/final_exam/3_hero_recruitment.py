heroes = {}

while True:
    cmd_line = input()
    if cmd_line == "End":
        break

    cmd_type, *info = cmd_line.split()
    hero_name = info[0]

    if cmd_type == "Enroll":
        if hero_name not in heroes:
            heroes[hero_name] = set()
        else:
            print(f"{hero_name} is already enrolled.")

    if cmd_type == "Learn":
        spell = info[1]
        if hero_name in heroes:
            if spell in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell}.")
            else:
                heroes[hero_name].add(spell)
        else:
            print(f"{hero_name} doesn't exist.")

    if cmd_type == "Unlearn":

        spell = info[1]
        if hero_name in heroes:
            if spell in heroes[hero_name]:
                heroes[hero_name].remove(spell)
            else:
                print(f"{hero_name} doesn't know {spell}.")
        else:
            print(f"{hero_name} doesn't exist.")

print("Heroes:")
for hero_name, spells in heroes.items():
    spell_list = ", ".join(sorted(spells))
    print(f"== {hero_name}: {spell_list}")