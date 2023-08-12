# HW: OOP. Inheritance

1. Create a class Product with properties name, price, and quantity. Create a child class Book that inherits from Product and adds a property author and a method called read that prints information about the book.

2. Create a class Restaurant with properties name, cuisine, and menu. The menu property should be a dictionary with keys being the dish name and values being the price. Create a child class FastFood that inherits from Restaurant and adds a property drive_thru (a boolean indicating whether the restaurant has a drive-thru or not) and a method called order, which takes in the dish name and quantity and returns the total cost of the order. The method should also update the menu dictionary to subtract the ordered quantity from the available quantity. If the dish is not available or if the requested quantity is greater than the available quantity, the method should return a message indicating that the order cannot be fulfilled. Example of usage:

    ```python
    class Restaurant:
        # your code here
        pass

    class FastFood(Restaurant):
        # your code here
        pass

    menu =  {
        'burger': {'price': 5, 'quantity': 10},
        'pizza': {'price': 10, 'quantity': 20},
        'drink': {'price': 1, 'quantity': 15}
    }

    mc = FastFood('McDonalds', 'Fast Food', menu, True)

    print(mc.order('burger', 5)) # 25
    print(mc.order('burger', 15)) # Requested quantity not available
    print(mc.order('soup', 5)) # Dish not available
    ```

3. (Optional) A Bank

    Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. A SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute and a method which adds interest to the account. A CurrentAccount object, in addition to the attributes of an Account object, should have an overdraft limit attribute.
    Now create a Bank class, an object of which contains an array of Account objects. Accounts in the array could be instances of the Account class, the SavingsAccount class, or the CurrentAccount class. Create some test accounts (some of each type).

    Write an update method in the Bank class. It iterates through each account, updating it in the following ways: Savings accounts get interest added (via the method you already wrote); CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).
    The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.

    ```python
    class Account:
        def __init__(self, balance, account_number):
            self._balance = balance
            self._account_number = account_number
        
        @classmethod
        def create_account(cls, account_number):
            return cls(0.0, account_number)
        
        def deposit(self, amount):
    ```    