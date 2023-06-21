# receive input for the countries on the first line, in form of a list
countries_list = input().split(", ")
# receive input for the capitals on the second line, in form of a list
capitals_list = input().split(", ")

# create a dictionary comprehension, zipping both lists
capitals_dict = {
    country: capital
    for country, capital in zip(countries_list, capitals_list)
}

# print the dictionary line by line according to the expected format
for country, capital in capitals_dict.items():
    print(f"{country} -> {capital}")
