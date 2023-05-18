n1 = int(input())
n2 = int(input())

lst = [
    n1*i
    for i in range(1, n2+1)
]

print(lst)