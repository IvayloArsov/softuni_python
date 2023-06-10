f = int(input())

for x in range(1, f + 1):
    for y in range(1, f + 1):
        for z in range(1, f + 1):
            for i in range(1, f + 1):
                if i < 10 and z < 10 and y < 10 and x < 10:
                    if f % x == 0 and f % y == 0 and f % z == 0 and f % i == 0:
                        print(f"{x}{y}{z}{i}", end=" ")

###########################################################
# another better solution:

f = int(input())

results = []

for x in range(1, 10):
    if f % x != 0:
        continue
    for y in range(1, 10):
        if f % y != 0:
            continue
        for z in range(1, 10):
            if f % z != 0:
                continue
            for i in range(1, 10):
                if f % i != 0:
                    continue
                results.append(f"{x}{y}{z}{i}")

print(" ".join(results))
