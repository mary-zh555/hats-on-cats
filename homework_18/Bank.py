class Account:
    def __init__(self, balance: float, account_number: str):
        self._balance = balance
        self._account_number = account_number

    # @classmethod
    # def create_account(cls, account_number):
    #     return cls(0.0, account_number)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


class SavingsAccount(Account):
    def __init__(self, balance: float, account_number: str, interest: float):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self):
        interest_earned = self._balance * self.interest
        self._balance += interest_earned


class CurrentAccount(Account):
    def __init__(self, balance: float, account_number: str, overdraft_limit: int):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self):
        if self._balance >= self.overdraft_limit:
            print(
                f"Account {self._account_number} has reached overdraft limit of {self.overdraft_limit}$. Current balance: {self._balance}$"
            )


class Bank:
    def __init__(self):
        self.accounts: list[Account] = []  # Create an empty list to store accounts

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account._account_number == account_number:
                print(f"Account {account_number} is removed.")
                return self.accounts.remove(account)
        raise ValueError("Account not found")

    # Annual updating
    def update_account(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.check_overdraft()

    def pay_dividend(self, dividend_amount):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.deposit(dividend_amount)

    def __str__(self):
        text: str = f"Bank have {len(self.accounts)} accounts: \n"
        for account in self.accounts:
            text += f"Account Number: {account._account_number}, Balance: {account._balance} \n"
        return text
