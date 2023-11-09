from task1 import validate_args
from task2 import memoize
import time


def timer(func):
    def wrapper(*args, **kwargs):
        nonlocal is_initial_call
        if is_initial_call:
            is_initial_call = False
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Функция {func.__name__} занимает {end_time - start_time} секунд.")
            is_initial_call = True
            return result
        else:
            return func(*args, **kwargs)

    is_initial_call = True
    return wrapper


@validate_args
@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@validate_args
@memoize
@timer
def fibonacci_memoized(n):
    if n < 2:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


print(fibonacci(30))
print(fibonacci_memoized(200))

