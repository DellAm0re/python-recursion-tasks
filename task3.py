
def fibonacci(n, cache=None):
    if cache is None:
        cache = {}

    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)

    return cache[n]


n = int(input("Введіть n: "))
print("Результат:", fibonacci(n))
  
