raw_spell = input()

cmd_line = input()
spells = ["Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]
while cmd_line != "Abracadabra":

    command, *info = cmd_line.split()

    if command not in spells:
        print("The spell did not work!")

    if command == "Abjuration":
        raw_spell = raw_spell.upper()
        print(raw_spell)
    if command == "Necromancy":
        raw_spell = raw_spell.lower()
        print(raw_spell)

    if command == "Illusion":
        idx, new_letter = info
        idx = int(idx)
        if 0 <= idx < len(raw_spell):
            old_letter = raw_spell[idx]
            raw_spell = raw_spell.replace(old_letter, new_letter, 1)

            print("Done!")
        else:
            print("The spell was too weak.")

    if command == "Divination":
        old_str, new_str = info
        if old_str == new_str or old_str not in raw_spell:
            pass
        else:
            raw_spell = raw_spell.replace(old_str, new_str)
            print(raw_spell)

    if command == "Alteration":
        substr = info[0]
        if substr in raw_spell:
            raw_spell = raw_spell.replace(substr, "")
            print(raw_spell)
        else:
            pass

    cmd_line = input()

