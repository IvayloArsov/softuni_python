import re

main_string = input()

patterns = re.compile(
    r"([|#])(?P<item_name>[A-Za-z\s]+)\1(?P<epx_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]+)\1")

# ([|#])(?P<item_name>[A-Za-z\s]+)\1(?P<epx_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]{1,}\1)

list_result = list()
result = re.finditer(patterns, main_string)
total = 0
for show in result:
    total += int(show["calories"])
    list_result.append({"name": show["item_name"], "date": show["epx_date"], "nutrition": show["calories"]})

total = int(total // 2000)

print(f"You have food to last you for: {total} days!")
for show in list_result:
    print(f"Item: {show['name']}, Best before: {show['date']}, Nutrition: {show['nutrition']}")