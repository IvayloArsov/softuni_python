nylon = 1.50
paint = 14.50
thinner = 5
bags = 0.4

nylon_sqm = (int(input())+2) * nylon
num_paint = (int(input())*1.1) * paint
num_thinner = int(input()) * thinner
workhours = int(input())
mats = bags + num_thinner + num_paint+nylon_sqm
worker_expense = (mats*0.30) * workhours
expenses = mats+worker_expense

print(expenses)