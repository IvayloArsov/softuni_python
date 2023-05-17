import math

set_record = float(input())
distance = float(input())
speed_m = float(input())

slowing = math.floor(distance/50)
slowing *= 30
george = distance*speed_m + slowing

if george < set_record:
    print(f" Yes! The new record is {george:.2f} seconds.")

else:
    print(f"No! He was {george-set_record:.2f} seconds slower.")