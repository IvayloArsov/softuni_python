targets = [int(num) for num in input().split()]
targets_shot = 0
while True:
    command = input()
    if command == 'End':
        break
    else:
        idx = int(command)
        if 0 <= idx < len(targets):
            if targets[idx] == -1:
                continue

            temp = targets[idx]
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] > temp:
                        targets[i] -= temp
                    else:
                        targets[i] += temp

            targets[idx] = -1
            targets_shot += 1

print(f"Shot targets: {targets_shot} -> {' '.join(str(num) for num in targets)}")