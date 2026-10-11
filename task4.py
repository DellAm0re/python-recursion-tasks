
def climb_stairs(n, cache=None):
    if cache is None:
        cache = {}

    if n == 1:
        return 1

    if n == 2:
        return 2

    if n in cache:
        return cache[n]

    cache[n] = climb_stairs(n - 1, cache) + climb_stairs(n - 2, cache)

    return cache[n]


n = int(input("Введіть кількість сходинок: "))
print("Кількість способів:", climb_stairs(n))
