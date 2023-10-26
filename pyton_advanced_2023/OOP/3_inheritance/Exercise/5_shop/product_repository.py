from project.product import Product
# from product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
        print(f"{product_name} not found in the repository.")
        return None

    def remove(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        print(f"{product_name} not found in the repository.")

    def __repr__(self):
        products_info = ""
        for product in self.products:
            products_info += f"{product.name}: {product.quantity}\n"
        return products_info.rstrip()
