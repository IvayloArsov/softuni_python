lines = int(input())
regular = set()
vip = set()
for _ in range(lines):
    res_code = input()
    if len(res_code) == 8:
        if res_code[0].isdigit():
            vip.add(res_code)
        else:
            regular.add(res_code)

while True:
    command = input()
    if command == "END":
        break
    if command in vip:
        vip.remove(command)
    elif command in regular:
        regular.remove(command)

missing_list = sorted(vip.union(regular))
print(len(missing_list))
print("\n".join(missing_list))