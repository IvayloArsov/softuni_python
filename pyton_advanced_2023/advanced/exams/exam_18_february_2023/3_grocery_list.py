def shop_from_grocery_list(budget, grocery_list, *products):
    bought_items = []

    for item in products:
        product, price = item
        if budget >= 0 and budget >= price:
            if product in grocery_list and product not in bought_items:
                bought_items.append(product)
                budget -= price
                grocery_list.remove(product)
        else:
            break
    if grocery_list:
        result = f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    else:
        result = f'Shopping is successful. Remaining budget: {budget:.2f}.'
    return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
