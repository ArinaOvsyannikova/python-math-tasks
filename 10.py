import math
s = input()
q = len(s)
n = math.ceil(math.sqrt(q))  # размерность матрицы
b = list(s[::-1])  # развернутая строка
flag, j, i, top, bot, left, right = 0, 0, 0, 0, n - 1, 0, n - 1
a = [[0 for _ in range(n)] for _ in range(n)]
for c in range(n * n):  # заполняем матрицу по спирали
    a[i][j] = c
    if i == bot and j == left:
        flag += 1
    if flag == 1 and i == (top + 1) and j == left and i != 0:
        left += 1
        top += 1
        bot -= 1
        right -= 1
        flag = 0
    if i == top and j < right:
        j += 1
    elif j == right and i < bot:
        i += 1
    elif i == bot and j > left:
        j -= 1
    else:
        i -= 1
# вывод
for c in range(n):
    for c2 in range(n):
        w = a[c][c2]
        if w > len(b) - 1:
            print("  ", end="")
        else:
            print(b[w], end=" ")
    print()
for c in range(n):
    for c2 in range(n):
        w = a[c][c2]
        if w > len(b) - 1:
            print(" ", end="")
        else:
            print(b[w], end=" ")
