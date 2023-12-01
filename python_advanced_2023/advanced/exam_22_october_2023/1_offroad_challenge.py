from collections import deque

nafta = list(map(int, input().split()))
razhod = deque(map(int, input().split()))
vurhove = deque(map(int, input().split()))
pokoreni_vurhove = 0
spisyk_vurhove = []

while vurhove:
    if not nafta or not razhod:
        print("John failed to reach the top.")
        if spisyk_vurhove:
            print("Reached altitudes: " + ", ".join(spisyk_vurhove))
        break

    cur_nafta = nafta.pop()
    cur_razhod = razhod.popleft()
    result = cur_nafta - cur_razhod
    cur_peak = vurhove[0]

    if result >= cur_peak:
        vurhove.popleft()
        pokoreni_vurhove += 1
        spisyk_vurhove.append(f"Altitude {pokoreni_vurhove}")
        print(f"John has reached: Altitude {pokoreni_vurhove}")
    else:
        print(f"John did not reach: Altitude {(pokoreni_vurhove + 1)}")
        print('John failed to reach the top.')
        if not spisyk_vurhove:
            print("John didn't reach any altitude.")
        else:
            print("Reached altitudes: " + ", ".join(spisyk_vurhove))
        break
else:
    print("John has reached all the altitudes and managed to reach the top!")
