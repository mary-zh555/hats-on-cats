# 1. Write a decorator that ensures a function is only called by users with a specific role. Each function should have an user_type with a string type in kwargs
# 2. Write a decorator that wraps a function in a try-except block and print an error if any error has happened


import questionary


def error_handler(func):
    def inner_function(*args, **kwargs):
        counter = 0
        try:
            func(*args, **kwargs)
        except Exception as e:
            counter += 1
            questionary.print(
                f"Found {counter} error during execution of your function: \n ⛔ {type(e).__name__}: {e}",
                style="bold fg:darkred",
            )

    return inner_function


def is_admin(func):
    def wrapper(user_type):
        if user_type == "admin":
            func(user_type)
        else:
            raise ValueError("Permission denied!")

    return wrapper


@error_handler
@is_admin
def show_customer_receipt(user_type: str):
    questionary.print(
        "⚠  Some very dangerous operation is initialized!", style="italic fg:yellow"
    )


@error_handler
def some_function_with_risky_operation(data):
    print(data["key"])


if __name__ == "__main__":
    show_customer_receipt(user_type="user")
    # > ValueError: Permission denied

    show_customer_receipt(user_type="admin")
    # > function pass as it should be

    some_function_with_risky_operation({"foo": "bar"})
    # > Found 1 error during execution of your function: KeyError no such key as foo

    some_function_with_risky_operation({"key": "bar"})
    # > bar

    some_function_with_risky_operation("data")
    # > TypeError: string indices must be integers, not 'str'
