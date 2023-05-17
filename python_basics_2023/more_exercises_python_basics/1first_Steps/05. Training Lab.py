desk_L = 0.7
desk_W = 1.2
l = float(input('дължина на стаята? : '))
w = float(input('широчина на залата? : '))
total_desks = (l//desk_W) * ((w-1)//desk_L) -3
print(total_desks)
