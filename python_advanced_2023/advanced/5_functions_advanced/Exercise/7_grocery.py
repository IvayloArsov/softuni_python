def grocery_store(**kwargs):
    result = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    results = []
    for product, quantity in result.items():
        results.append(f"{product}: {quantity}")

    return "\n".join(results)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))