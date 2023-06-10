holidays = int(input())
workdays = 365 - holidays
playime = 30_000
w_play = 63
h_play = 127
total_play = holidays*h_play + workdays*w_play

if total_play>playime:
    print("Tom will run away")
    print(f"{(total_play-playime)//60} hours and {(total_play-playime)%60} minutes more for play")
else:
    print('Tom sleeps well')
    print(f"{(playime-total_play)//60} hours and {(playime%total_play)%60} minutes less for play")