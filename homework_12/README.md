## HW: Decorator

1. Write a decorator that ensures a function is only called by users with a specific role. Each function should have an user_type with a string type in kwargs

    Example

    ```python
    @is_admin
    def show_customer_receipt(user_type: str):
        # some very dangerous operation

    show_customer_receipt(user_type='user')
    > ValueError: Permission denied

    show_customer_receipt(user_type='admin')
    > function pass as it should be
    ```

2. Write a decorator that wraps a function in a try-except block and print an error if any error has happened

    Example
    ```python
    
    @catch_errors
    def some_function_with_risky_operation(data):
        print(data['key'])


    some_function_with_risky_operation({'foo': 'bar'})
    > Found 1 error during execution of your function: KeyError no such key as foo

    some_function_with_risky_operation({'key': 'bar'})
    > bar
    ```

3. Optional: Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations. It should work for all possible functions. Don’t forget to check the return type as well.

    Example:

    ```python
    @check_types
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    > 3

    add("1", "2")
    > TypeError: Argument a must be int, not str

    ```

4. Optional: Create a function that caches the result of a function, so that if it is called with the same argument multiple times, it returns the cached result first instead of re-executing the function.


5. Optional: Write a decorator that adds a rate-limiter to a function, so that it can only be called a certain amount of times per minute.