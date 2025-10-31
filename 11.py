def nam(n):
    s = 0
    k = 0
    while n != 0:
        k += 1
        s += n % 10
        n //= 10
    return s, k

a = int(input("введите число: "))
s, k = nam(a)
print(f"сумма цифр: {s}, количество цифр: {k}")
