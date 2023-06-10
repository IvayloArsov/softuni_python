extra_chairs = []
enough_chairs = True
for event in range(1, int(input())+1):
    insufficient = []
    chairs, people = input().split()
    people = int(people)
    if len(chairs) > people:
        for _ in range(len(chairs)-people):
            extra_chairs.append("X")
    else:
        insufficient += [1 for _ in range(people-len(chairs))]
    if len(insufficient) > 0:
        enough_chairs = False
        print(f"{len(insufficient)} more chairs needed in room {event}")

if enough_chairs:
    print(f"Game On, {len(extra_chairs)} free chairs left")