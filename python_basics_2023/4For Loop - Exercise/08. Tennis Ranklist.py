import math

t = int(input())
pts_start = int(input())

pts = 0 + pts_start
tour_pts = 0
wins = 0
for i in range(t):
    final = input()

    if final == 'W':
        tour_pts = 2000
        pts += tour_pts
        wins += 1
    elif final == 'F':
        tour_pts = 1200
        pts += tour_pts
    elif final == 'SF':
        tour_pts = 720
        pts += tour_pts

print(f"Final points: {pts}")
print(f"Average points: {math.floor((pts - pts_start) / t):.0f}")
print(f"{wins * 100 / t:.2f}%")
