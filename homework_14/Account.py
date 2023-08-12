class Account:
    def __init__(self, balance: float, account_number: str):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        pass


class SavingsAccount(Account):
    def __init__(self, balance: float, account_number: str, interest: float):
        super().__init__(balance, account_number)
        self.interest = interest


class CurrentAccount(Account):
    def __init__(self, balance: float, account_number: str, overdraft_limit: int):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit
