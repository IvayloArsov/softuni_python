class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(str(product_name))

    def get_by_letter(self, first_letter: str):
        selected = [product for product in self.products if product.casefold().startswith(first_letter.casefold())]
        return selected

    def __repr__(self):
        show_result = "Items in the {0} catalogue:\n" \
                 "{1}".format(self.name, '\n'.join(sorted(self.products)))
        return show_result


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("d"))
# print(catalogue)
