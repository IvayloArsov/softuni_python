start_interval_digit = int(input())
end_interval_digit = int(input())

for i in range(start_interval_digit, end_interval_digit + 1):
    for x in range(start_interval_digit, end_interval_digit + 1):
        for y in range(start_interval_digit, end_interval_digit + 1):
            for q in range(start_interval_digit, end_interval_digit + 1):
                if i > q:
                    if (x+y)%2 == 0:
                        if i % 2 == 0 and q % 2 != 0:
                            print(f"{i}{x}{y}{q}", end=' ')
                        elif q % 2 == 0 and i % 2 !=0:
                            print(f"{i}{x}{y}{q}", end=' ')



