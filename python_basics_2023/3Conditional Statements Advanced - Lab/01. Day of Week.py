userinput = int(input())
week ={
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
}

if userinput>=1 and userinput<=7:
    print(week[userinput])
else:
    print('Error')