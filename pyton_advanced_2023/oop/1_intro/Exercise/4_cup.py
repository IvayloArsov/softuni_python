class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int):
        difference = self.size - self.quantity
        if quantity <= difference:
            self.quantity += quantity

    def status(self):
        difference = self.size - self.quantity
        return difference


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
