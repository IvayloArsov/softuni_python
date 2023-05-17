tabs = int(input())
salary = int(input())

for i in range(tabs):
    open_tab = input()
    if open_tab == 'Facebook':
        salary -= 150
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif open_tab == 'Instagram':
        salary -= 100
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif open_tab == 'Reddit':
        salary -= 50
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(salary)
