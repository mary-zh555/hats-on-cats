from Product import Book
from Restaurant import FastFood
from Bank import Bank, SavingsAccount, CurrentAccount


def name_task(func):
    def wrapper():
        message = f"---- {func.__name__} ----"
        print(message)
        func()
        print(f"{'-'*len(message)}")

    return wrapper


@name_task
def task_1():
    code_simplicity = Book("Code Simplicity", 0, 2, "Max Kanat-Alexander")
    print(code_simplicity)


### Task 2
@name_task
def task_2():
    menu = {
        "burger": {"price": 5, "quantity": 10},
        "pizza": {"price": 10, "quantity": 20},
        "drink": {"price": 1, "quantity": 15},
    }

    mc = FastFood("McDonalds", "Fast Food", menu, True)

    print(mc.order("burger", 5))  # 25
    print(mc.order("burger", 15))  # Requested quantity not available
    print(mc.order("soup", 5))  # Dish not available


### Task 3
@name_task
def task_3():
    bank = Bank()

    # Creating instances of SavingsAccount and CurrentAccount
    savings1 = SavingsAccount(1000.0, "SAV001", 0.03)
    savings2 = SavingsAccount(1500.0, "SAV002", 0.04)
    savings3 = SavingsAccount(2000.0, "SAV003", 0.03)
    current1 = CurrentAccount(500.0, "CUR001", 1000)
    current2 = CurrentAccount(1000.0, "CUR002", 1500)
    current3 = CurrentAccount(1300.0, "CUR003", 1200)
    accounts = [savings1, savings2, savings3, current1, current2, current3]

    for account in accounts:
        bank.open_account(account)

    print(bank)

    bank.open_account(SavingsAccount(2000.0, "SAV004", 0.05))
    bank.open_account(CurrentAccount(350.0, "CUR004", 1500))

    bank.close_account("CUR001")
    bank.update_account()

    print(bank)


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
