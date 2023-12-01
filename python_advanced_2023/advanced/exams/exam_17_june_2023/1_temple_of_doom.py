from collections import deque

tools = deque(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while tools and substances and challenges:

    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_substance * current_tool

    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print("Tools:", ", ".join(map(str, tools)))
if substances:
    print("Substances:", ", ".join(map(str, substances)))
if challenges:
    print("Challenges:", ", ".join(map(str, challenges)))
