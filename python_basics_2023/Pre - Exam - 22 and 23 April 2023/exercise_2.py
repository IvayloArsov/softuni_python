t_shirt = float(input())
ball = float(input())
shorts = t_shirt*0.75
socks = shorts*0.20
shoes = (t_shirt+shorts)*2

total = (t_shirt+shoes+socks+shorts)*0.85

if total >= ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {ball-total:.2f} lv. more.")