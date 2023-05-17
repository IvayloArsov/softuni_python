group = int(input())
season = input()
price = 0

if group <= 5:
    if season == "spring":
        price = 50.00
    if season == "summer":
        price = 48.50
    if season == "autumn":
        price = 60.00
    if season == "winter":
        price = 86.00
if group > 5:
    if season == "spring":
        price = 48.00
    if season == "summer":
        price = 45.00
    if season == "autumn":
        price = 49.50
    if season == "winter":
        price = 85.00

total = group * price
if season == "summer":
    total *= 0.85
if season == "winter":
    total *= 1.08

print(f"{total:.2f} leva.")

