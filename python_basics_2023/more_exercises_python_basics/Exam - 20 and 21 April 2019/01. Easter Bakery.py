p_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
c_eggs = int(input())
yeast = int(input())

price_sugar = p_flour * 0.75
price_eggs = p_flour * 1.10
price_yeast = price_sugar * 0.20

total = (p_flour*kg_flour)+kg_sugar*price_sugar+c_eggs*price_eggs+yeast*price_yeast

print(f'{total:.2f}')