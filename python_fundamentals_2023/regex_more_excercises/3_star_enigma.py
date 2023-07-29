import re

lines = input()
key = r"(?i)[star]"
second_key = re.compile(
    r"@(?P<planet>[A-Za-z]+)([^\@\-\!\:\>]*)"
    r":(?P<population>\d+)([^\@\-\!\:\>]*)"
    r"\!(?P<attack>[AD])!([^\@\-\!\:\>]*)"
    r"->(?P<soldiers>\d+)"
)

attacked_planets = []
destroyed_planets = []

for line in range(int(lines)):
    encrypted_msg = input()
    key_matches = re.findall(key, encrypted_msg)
    reduction_value = int(len(key_matches))
    decrypted = [chr(ord(element) - reduction_value) for element in encrypted_msg]
    decrypted_line = "".join(decrypted)
    matches = re.finditer(second_key, decrypted_line)
    for match in matches:
        if match["attack"] == "A":
            attacked_planets.append(match["planet"])
        elif match["attack"] == "D":
            destroyed_planets.append(match["planet"])
print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")