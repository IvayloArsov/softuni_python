cargos = int(input())
total_tonnage = 0
money = 0
bus = 0
truck = 0
train = 0
for i in range(0, cargos):

    tonnage = int(input())

    if tonnage >= 12:
        train += tonnage
        money += tonnage*120
    elif 11 >= tonnage >= 4:
        truck += tonnage
        money += tonnage*175
    elif tonnage <= 3:
        bus += tonnage
        money += tonnage*200

    total_tonnage += tonnage

print(f'{money/total_tonnage:.2f}')
print(f'{(bus/total_tonnage)*100:.2f}%')
print(f'{(truck/total_tonnage)*100:.2f}%')
print(f'{(train/total_tonnage)*100:.2f}%')
