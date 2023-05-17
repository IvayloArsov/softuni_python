company = input()
tickets_adults = int(input())
tickets_children = int(input())
price_adult = float(input())
price_service = float(input())

total = (tickets_adults*(price_adult+price_service))+(tickets_children*((price_adult*0.30)+price_service))
profit = total * 0.20
print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")