import math

x = float(input("введите х: "))
n = int(input("введите кол-во слогаемых: "))

if abs(x) > 1:
    c = x  # предыдущее значение
    f = 1  # коэфициент
    s = 1 / x  # сумма

    for i in range(1, n):
        c = c * x * x * (f + 2) / f
        s += 1 / c
        f += 2
    print(s)
else:
    print("введенное значение недопустимо")
