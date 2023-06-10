month = input()
nights = int(input())
studio = 0
flat = 0

if month == 'May' or month == 'October':
    studio = 50
    flat = 65
    if nights > 14:
        studio *= 0.70
    elif nights > 7:
        studio *= 0.95
elif month == 'June' or month == 'September':
    studio = 75.20
    flat = 68.70
    if nights > 14:
        studio *= 0.80
elif month == 'July' or month == 'August':
    studio = 76
    flat = 77

if nights > 14:
    flat *= 0.90

price_flat = nights * flat
price_studio = nights * studio

print(f"Apartment: {price_flat:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
