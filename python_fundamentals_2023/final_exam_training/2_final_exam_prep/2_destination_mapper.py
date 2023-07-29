import re

pattern = re.compile(
    r"(?P<break>[=|/])"
    r"(?P<destination>[A-Z][a-zA-Z]{2,})\1"
)
destinations = []
cmd_input = input()
matches = re.finditer(pattern, cmd_input)
for match in matches:
    if match["destination"]:
        destinations.append(match["destination"])

total_length = sum(len(word) for word in destinations)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_length}")