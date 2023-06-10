vegetable = float(input('vegetables price:'))
fruits = float(input('fruit price: '))
veg_kg = int(input('vegetable kilos: '))
fru_kg = int(input('fruits kilos: '))
euro = 1.94
veg_sum = veg_kg*vegetable
fru_sum = fru_kg*fruits
total = (veg_sum+fru_sum)/euro
print(total)