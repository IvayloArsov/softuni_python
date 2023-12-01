from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    loan_types = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan
    }
    client_types = {
        'Student': Student,
        'Adult': Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.loan_types.keys():
            raise Exception("Invalid loan type!")
        new_loan = self.loan_types[loan_type]()
        self.loans.append(new_loan)
        info_str = f'{loan_type} was successfully added.'
        return info_str

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.client_types.keys():
            raise Exception('Invalid client type!')
        if len(self.clients) < self.capacity:
            new_client = self.client_types[client_type](client_name, client_id, income)
            self.clients.append(new_client)
            info_str = f'{client_type} was successfully added.'
            return info_str
        else:
            return 'Not enough bank capacity.'

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_id(client_id)
        loan = self.find_loan_by_type(loan_type)
        if client.TYPE_ != loan.TYPE_CLIENT:
            raise Exception('Inappropriate loan type!')
        self.loans.remove(loan)
        client.loans.append(loan)
        info_str = f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        return info_str

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)
        if not client:
            raise Exception('No such client!')
        if client.loans:
            raise Exception('The client has loans! Removal is impossible!')
        self.clients.remove(client)
        info_str = f'Successfully removed {client.name} with ID {client_id}.'
        return info_str

    def increase_loan_interest(self, loan_type: str):
        changed_interest_loans_counter = 0
        for loan in self.loans:
            if loan.TYPE_ == loan_type:
                loan.increase_interest_rate()
                changed_interest_loans_counter += 1
        info_str = f'Successfully changed {changed_interest_loans_counter} loans.'
        return info_str

    def increase_clients_interest(self, min_rate: float):
        affected_clients = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                affected_clients += 1
        info_str = f"Number of clients affected: {affected_clients}."
        return info_str

    def get_statistics(self):
        total_clients_income = sum([x.income for x in self.clients])
        loans_count_granted_to_clients = len(
            [
                loan
                for client in self.clients
                for loan in client.loans if client.loans
            ]
        )
        granted_sum = sum(
            [
                loan.AMOUNT
                for client in self.clients
                for loan in client.loans if client.loans
            ]
        )
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])
        # This following bit is very important for edge cases where the input is 0 :)
        avg_client_interest_rate = (
                sum([client.interest for client in self.clients]) / len(self.clients)
        ) if len(self.clients) > 0 else 0

        info_list = [
            f"Active Clients: {len(self.clients)}",
            f"Total Income: {total_clients_income:.2f}",
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}",
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        ]

        return '\n'.join(info_list)

    def find_client_by_id(self, client_id):
        """
        Helper function, facilitating finding the client by client_id, returns the first match
        :param client_id:
        :return:
        """
        clients = [client for client in self.clients if client.client_id == client_id]
        return clients[0] if clients else None

    def find_loan_by_type(self, loan_type):
        """
        Helper function, facilitating finding the loan by its type, returns the first match
        :param loan_type:
        :return:
        """
        loans = [loan for loan in self.loans if loan.TYPE_ == loan_type]
        return loans[0]
