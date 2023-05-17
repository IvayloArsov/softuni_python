annual_fee = int(input())
shoes = annual_fee-(annual_fee*0.4)
clothes = shoes-(shoes*0.2)
ball = clothes*0.25
accessories = ball * 0.2
total = annual_fee+shoes+clothes+ball+accessories
print(total)