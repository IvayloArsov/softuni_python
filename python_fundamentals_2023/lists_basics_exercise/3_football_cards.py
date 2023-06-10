new_list = list(input().split(" "))
a_team = []
b_team = []
flag = False
for element in new_list:
    if element[0] == 'A':
        if element not in a_team:
            a_team.append(element)
    elif element[0] == 'B':
        if element not in b_team:
            b_team.append(element)
    if len(a_team) > 4 or len(b_team) > 4:
        flag = True
        break


print(f"Team A - {11 -len(a_team)}; Team B - {11 - len(b_team)}")
if flag:
    print('Game was terminated')
