length = int(input())
width = int(input())
height = int(input())
filled = float(input())/100
fulltank = (length*width*height)/1000
neededLitres = fulltank*(1-filled)

print(neededLitres)