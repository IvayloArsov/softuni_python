n = int(input())
students = dict()
for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name in students.keys():
        students[name].append(grade)
    else:
        students[name] = [grade]

for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")
