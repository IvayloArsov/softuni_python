userinput = str(input())

week ={
    'Monday':'Working day',
    'Tuesday':'Working day',
    'Wednesday':'Working day',
    'Thursday':'Working day',
    'Friday':'Working day',
    'Saturday':'Weekend',
    'Sunday':'Weekend'
}

if userinput in week.keys():
    print(week[userinput])
else:
    print('Error')