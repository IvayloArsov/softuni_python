userinput = input()
price = 0
if userinput == 'Monday' or userinput == 'Tuesday' or userinput == 'Friday':
    price = 12
    print(price)
elif userinput == 'Wednesday' or userinput == 'Thursday':
    price = 14
    print(price)
elif userinput == 'Saturday' or userinput == 'Sunday':
    price = 16
    print(price)