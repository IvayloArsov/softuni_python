n = int(input('square side in meters: '))
w = float(input('tile width: '))
l = float(input('tile len: '))
m = int(input('bench width: '))
o = int(input('bench len: '))

tile = w * l
bench = m*o
square_m = n**2 - bench
tiles = square_m/tile
mins = tiles*0.2
print(tiles)
print(mins)
