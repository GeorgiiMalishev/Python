def memoize(func):
    cache = dict()

    def wrapper(*n):
        if n in cache:
            return cache[n]
        else:
            result = func(*n)
            cache[n] = result
            return result

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(250))
