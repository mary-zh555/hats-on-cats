# 3. Optional: Create a decorator that will check types.
# It should take a function with arguments and validate inputs with annotations.
# It should work for all possible functions. Don’t forget to check the return type as well.


def check_types(func):
    def wrapper(*args):
        annt = func.__annotations__
        func_return_type = type(func(*args))
        message = ""
        right_sumbol = "✅\n"
        wrong_symbol = "❌\n"

        for i, (k, v) in enumerate(annt.items()):
            arg = args[i]
            message += f"ATTRIBUTE {k}={repr(arg)} type got {type(arg)}, expected {v}"
            if (type(arg) == v) and (func_return_type == annt["return"]):
                message += right_sumbol
            else:
                message += wrong_symbol

            if i == len(args) - 1:
                break

        if func_return_type != annt["return"]:
            message += f"RETURN type don't match: got {func_return_type}, expected {annt['return']}❌\n"
        else:
            message += f"RETURN type match: got {func_return_type}, expected {annt['return']}✅\n"

        print(message)

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
# > 3

add("1", "2")
# > TypeError: Argument a must be int, not str
