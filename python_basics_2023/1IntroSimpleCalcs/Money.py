EUR = 1.95
USD = 1.76
CNY = USD*.15
BTC = 1168

btc_onhand = int(input())
cny_onhand = float(input())
comission = (1- float(input())/100)

exchanged = (((btc_onhand*BTC) + (cny_onhand*CNY)) *comission ) /EUR
print(f'{exchanged:.2f}')