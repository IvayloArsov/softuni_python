rent = int(input())

statues = rent * 0.70
catering = statues * 0.85
sound_ = catering / 2

expenses = rent + statues + catering + sound_

print(f'{expenses:.2f}')