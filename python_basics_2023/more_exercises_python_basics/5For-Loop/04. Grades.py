num_students = int(input())
excellent = 0
good = 0
mediocre = 0
fail = 0
total = 0
for n in range(0, num_students):
    grade = float(input())

    if grade >= 5:
        excellent += 1
    elif grade >= 4:
        good += 1
    elif grade >= 3:
        mediocre += 1
    elif grade < 3:
        fail += 1

    total += grade

avg = total/num_students
print(f"Top students: {excellent/num_students*100:.2f}%")
print(f"Between 4.00 and 4.99: {good/num_students*100:.2f}%")
print(f"Between 3.00 and 3.99: {mediocre/num_students*100:.2f}%")
print(f"Fail: {fail/num_students*100:.2f}%")
print(f"Average: {avg:.2f}")
