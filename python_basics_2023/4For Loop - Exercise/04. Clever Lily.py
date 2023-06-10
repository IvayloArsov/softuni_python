age = int(input())
washing_machine = float(input())
toy = int(input())
savings = 0
bdaymoney = 10
toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        savings += (bdaymoney - 1)
        bdaymoney += 10
    else:
        toys += 1
savings += toys * toy

print(f"Yes! {savings - washing_machine:.2f}" if savings >= washing_machine
      else f'No! {washing_machine - savings:.2f}')
