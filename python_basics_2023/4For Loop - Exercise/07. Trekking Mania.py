n = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
trekkers = 0

for index in range(0, n):
    current_num = int(input())
    trekkers += current_num

    if current_num <= 5:
        musala += current_num
    elif current_num <= 12:
        montblanc += current_num
    elif current_num <= 25:
        kilimanjaro += current_num
    elif current_num <= 40:
        k2 += current_num
    else:
        everest += current_num

p1_percentage = musala * 100 / trekkers
p2_percentage = montblanc * 100 / trekkers
p3_percentage = kilimanjaro * 100 / trekkers
p4_percentage = k2 * 100 / trekkers
p5_percentage = everest * 100 / trekkers

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')
