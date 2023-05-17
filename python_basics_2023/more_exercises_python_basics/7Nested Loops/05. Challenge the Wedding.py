men = int(input())
women = int(input())
tables = int(input())
table_counter = 1
for x in range(1, men+1):
    for y in range(1, women+1):
        if table_counter > tables:
            break
        else:
            print(f'({x} <-> {y})', end=' ')
        table_counter += 1

