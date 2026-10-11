
def my_pow(x, n):
    if n == 0:
        return 1.0

    if n < 0:
        if x == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return 1 / my_pow(x, -n)

    half = my_pow(x, n // 2)

    if n % 2 == 0:
        return half * half

    return x * half * half


x = float(input("Введіть x: "))
n = int(input("Введіть n: "))

print(f"Результат: {my_pow(x, n):.5f}")
