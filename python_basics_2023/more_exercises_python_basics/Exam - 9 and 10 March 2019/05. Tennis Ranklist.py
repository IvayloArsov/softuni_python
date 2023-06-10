import math

tourneys = int(input())
starting_pts = int(input())
pts = 0
wins = 0
total_tour_pts = 0 + starting_pts

for score in range(tourneys):
    stage_reached = input()

    if stage_reached == 'W':
        pts = 2000
        wins += 1
    elif stage_reached == 'F':
        pts = 1200
    elif stage_reached == 'SF':
        pts = 720
    total_tour_pts += pts

print(f"Final points: {total_tour_pts}")
print(f"Average points: {math.floor((total_tour_pts-starting_pts)/tourneys)}")
print(f"{wins/tourneys*100:.2f}%")