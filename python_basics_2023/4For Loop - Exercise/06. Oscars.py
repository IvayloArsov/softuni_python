nominee = input()
start_pts = float(input())
num_ppl = int(input())

needed_pts = 0

for i in range(num_ppl):
    name = input()
    pts = float(input())
    needed_pts = 1250.5
    start_pts += ((len(name) * pts) / 2)
    if start_pts >= needed_pts:
        print(f"Congratulations, {nominee} got a nominee for leading role with {start_pts:.1f}!")
        break
if start_pts < needed_pts:
    print(f"Sorry, {nominee} you need {needed_pts - start_pts:.1f} more!")
