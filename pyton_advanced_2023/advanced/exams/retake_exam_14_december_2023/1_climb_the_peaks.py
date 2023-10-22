from collections import deque

food_portions = list(map(int, input().split(', ')))
stamina = deque(map(int, input().split(', ')))
conquered_peaks = []
peaks = deque(
    [('Vihren', 80),
     ('Kutelo', 90),
     ('Banski Suhodol', 10),
     ('Polezhan', 60),
     ('Kamenitza', 70)]
)
for day in range(7):
    peak, difficulty = peaks[0]
    cur_food = food_portions.pop()
    cur_stamina = stamina.popleft()
    product = cur_stamina + cur_food

    if product >= difficulty:
        conquered_peaks.append(peak)
        peaks.popleft()
        if not peaks:
            break
    else:
        continue

if conquered_peaks:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    else:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    print('Conquered peaks:')
    [print(x) for x in conquered_peaks]
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
