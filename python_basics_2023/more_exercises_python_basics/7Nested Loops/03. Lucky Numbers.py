lucky_num = int(input())

for i in range(1, 10):
    for x in range(1, 10):
        for y in range(1, 10):
            for q in range(1, 10):
                if i+x == y+q:
                    if lucky_num % (i+x) == 0:
                        print(f"{i}{x}{y}{q}", end=' ')