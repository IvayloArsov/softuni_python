budget = float(input())
season = input()

destination = ''
holiday = ''
spent = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        holiday = 'Camp'
        spent = budget * 0.30
    elif season == 'winter':
        holiday = 'Hotel'
        spent = budget * 0.70
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        holiday = 'Camp'
        spent = budget * 0.40
    elif season == 'winter':
        holiday = 'Hotel'
        spent = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    holiday = 'Hotel'
    spent = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{holiday} - {spent:.2f}")
