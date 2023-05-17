days = int(input())
total = 0
for _ in range(days):
    price = float(input())
    days = int(input())
    capsules = int(input())
    sub_total = price * days * capsules

    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        total += sub_total
        print(f'The price for the coffee is: ${sub_total:.2f}')

print(f'Total: ${total:.2f}')
