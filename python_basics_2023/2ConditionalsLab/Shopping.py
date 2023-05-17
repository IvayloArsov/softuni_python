budget = float(input())
vga = int(input())
cpu = int(input())
ram = int(input())

pr_vga = 250*vga
pr_cpu = (pr_vga*0.35)*cpu
pr_ram = (pr_vga*0.10)*ram
total_sum = pr_vga+pr_cpu+pr_ram

if vga > cpu:
    total_sum = total_sum*0.85

if budget >= total_sum:
    print(f"You have {budget-total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum-budget:.2f} leva more!")