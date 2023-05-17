import math
proj_hours = int(input())
days = int(input())
workers = int(input())
effective_days = days*0.90
work_hours = effective_days*10*workers
if proj_hours > work_hours:
    unreached = proj_hours - work_hours
    print(f"Not enough time!{math.ceil(unreached)} hours needed.")
else:
    reached = work_hours - proj_hours
    print(f"Yes!{math.ceil(reached)} hours left.")