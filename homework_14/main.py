from Product import Book
from Restaurant import FastFood

if __name__ == "__main__":
    ## Task 1
    code_simplicity = Book("Code Simplicity", 0, 2, "Max Kanat-Alexander")

    # Task 2
    menu = {
        "burger": {"price": 5, "quantity": 10},
        "pizza": {"price": 10, "quantity": 20},
        "drink": {"price": 1, "quantity": 15},
    }

    mc = FastFood("McDonalds", "Fast Food", menu, True)

    print(mc.order("burger", 5))  # 25
    print(mc.order("burger", 15))  # Requested quantity not available
    print(mc.order("soup", 5))  # Dish not available

    # Task 3
