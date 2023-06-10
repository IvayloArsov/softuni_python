numbers = input().split(", ")

counter = 0
new_list = []
for num in numbers:
    if int(num) == 0:
        counter += 1
        continue
    new_list.append(int(num))
for _ in range(counter):
    new_list.append(0)
print(new_list)
