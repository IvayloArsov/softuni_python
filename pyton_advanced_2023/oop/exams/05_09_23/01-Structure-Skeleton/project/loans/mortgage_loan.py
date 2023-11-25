from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    RATE = 3.5
    AMOUNT = 50_000
    TYPE_ = 'MortgageLoan'
    TYPE_CLIENT = 'Adult'

    def __init__(self):
        super().__init__(interest_rate=self.RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
