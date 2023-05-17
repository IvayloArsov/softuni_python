year = int(input())

while True:
    year += 1
    year_ = set(str(year))
    if len(year_) == len(str(year)):
        break

print(year)
