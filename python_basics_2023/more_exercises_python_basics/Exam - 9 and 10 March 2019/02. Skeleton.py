minutes = int(input())
seconds = int(input())
meters = float(input())
speed_in_sec = float(input())

time_to_break = minutes*60 + seconds
slowing = (meters/120)*2.5
his_time = (meters/100)*speed_in_sec - slowing

if his_time <= time_to_break:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f'His time is {his_time:.3f}.')
else:
    print(f"No, Marin failed! He was {his_time-time_to_break:.3f} second slower.")