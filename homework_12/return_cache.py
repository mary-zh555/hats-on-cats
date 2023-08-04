# 4. Optional: Create a function that caches the result of a function,
# so that if it is called with the same argument multiple times,
# it returns the cached result first instead of re-executing the function.

from functools import cache
import time


memo = {}


def manual_cache(func):
    def wrapper(arg):
        if arg not in memo:
            memo[arg] = func(arg)
        return memo[arg]

    return wrapper


@manual_cache
def fib_1(n):
    st = time.time()  # get the start time

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_1(n - 1) + fib_1(n - 2)

        et = time.time()  # get the end time
        elapsed_time = (et - st) * 1000  # get the execution time in milliseconds
        print("FIB_1 : Execution time:", elapsed_time, "seconds")

        return result


# @manual_cache
def fib_2(n):
    st = time.time()  # get the start time
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_2(n - 1) + fib_2(n - 2)

        et = time.time()  # get the end time
        elapsed_time = (et - st) * 1000  # get the execution time in milliseconds
        print("FIB_2: Execution time:", elapsed_time, "seconds")

        return result


if __name__ == "__main__":
    print(fib_1(7))

    print(fib_2(7))
