import math

series = str(input())
len_episode = int(input())
len_break = int(input())
rest = len_break*1/4
lunch = len_break*1/8
freetime = len_break-(rest+lunch)

if len_episode <= freetime:
    print(f"You have enough time to watch {series} and left with {math.ceil(freetime-len_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(abs(freetime-len_episode))} more minutes.")