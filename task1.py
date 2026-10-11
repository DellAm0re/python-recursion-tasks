
def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s [0]


text = input("Введіть рядок: ")
print("Результат:", reverse_string(text))
