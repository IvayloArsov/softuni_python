sub_string = ["Sand", "Water", "Fish", "Sun"]
main_string = input().casefold()
placeholder_var = 0
for element in sub_string:
    placeholder_var += main_string.count(element.casefold())


print(placeholder_var)