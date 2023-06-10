eur= 1.95
usd = 1.76

btc = int(input())*1168
cny = float(input()) * 0.15 *1.76
tax = float(input())/100

total = (btc+cny)/eur
total -= (total*tax)

print(f"{total:.2f}")

