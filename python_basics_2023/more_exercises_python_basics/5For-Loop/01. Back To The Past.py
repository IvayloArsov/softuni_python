money = float(input())
year = int(input())-1800

for i in range(0,year+1):
    if i%2==0:
        money -= 12_000
    else:
        money -= 12_000 + ((18+i)*50)
if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {-money:.2f} dollars to survive.")