
from functools import wraps

def memoize_decorator(fibonacci):
    cache = {}

    @wraps(fibonacci)
    def wrapper(x):
        if x in cache:
            print(f'Cache hit for fibonacci({x})')
            return cache[x]

        result = fibonacci(x)
        print(f'Computed fibonacci({x}) = {result}')
        cache[x] = result
        return result

    return wrapper


@memoize_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
ans = fibonacci(n)
print(f'Final Result: {ans}')
