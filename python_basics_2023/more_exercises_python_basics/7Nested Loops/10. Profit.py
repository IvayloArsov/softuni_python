ones = int(input())
twos = int(input())
fivers = int(input())
price_to_pay = int(input())

for one in range(0, ones+1):
    for two in range(0, twos+1):
        for five in range(0, fivers+1):
            if (one*1)+(two*2)+(five*5) == price_to_pay:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {price_to_pay} lv.")