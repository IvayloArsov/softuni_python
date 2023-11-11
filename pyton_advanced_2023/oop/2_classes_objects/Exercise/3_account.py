class Account:
    def __init__(self, id: int, name: str, balance: int = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return f'Amount exceeded balance'

    def info(self):
        info_str = f'User {self.name} with account {self.id} has {self.balance} balance'
        return info_str


account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())