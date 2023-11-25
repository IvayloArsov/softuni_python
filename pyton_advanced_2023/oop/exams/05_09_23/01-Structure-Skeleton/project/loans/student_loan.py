from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    RATE = 1.5
    AMOUNT = 2000
    TYPE_ = 'StudentLoan'
    TYPE_CLIENT = 'Student'

    def __init__(self):
        super().__init__(interest_rate=self.RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2
