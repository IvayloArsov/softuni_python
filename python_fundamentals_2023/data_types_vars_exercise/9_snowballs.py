ball_list = []
b_w, b_t, b_q, b_v = 0, 0, 0, 0

for ball in range(int(input())):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    ball_list.append(value)
    if value >= max(ball_list):
        b_w = weight
        b_t = time
        b_q = quality
        b_v = value

print(f"{b_w} : {b_t} = {b_v:.0f} ({b_q})")
