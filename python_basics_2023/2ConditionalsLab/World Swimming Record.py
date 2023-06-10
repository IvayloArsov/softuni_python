import math

world_record = float(input())
distance = float(input())
speed = float(input())
slowing = math.floor(distance//15)*12.5
ivans_time = slowing+(distance*speed)

if ivans_time < world_record:
    print(f" Yes, he succeeded! The new world record is {ivans_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(ivans_time-world_record):.2f} seconds slower.")