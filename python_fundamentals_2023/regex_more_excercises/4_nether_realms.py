import re


def calculate_health(name):
    health_chars = re.findall(r'[^\d\+\-\*\/\.]', name)
    health = sum(ord(char) for char in health_chars)
    return health


def calculate_damage(name):
    numbers = re.findall(r'(?:[-+]?\d+(?:\.\d+)?)', name)
    damage = sum(float(num) for num in numbers)
    for operation in re.findall(r'[*\/]', name):
        if operation == '*':
            damage *= 2
        elif operation == '/':
            damage /= 2
    return damage


demon_names_input = input()
demon_names = re.split(r'\s*,\s*', demon_names_input)

demons = []
for name in demon_names:
    health = calculate_health(name)
    damage = calculate_damage(name)
    demons.append((name, health, damage))

sorted_demons = sorted(demons, key=lambda x: x[0])

for demon in sorted_demons:
    name, health, damage = demon
    print(f"{name} - {health} health, {damage:.2f} damage")