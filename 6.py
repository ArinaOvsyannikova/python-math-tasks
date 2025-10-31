n = int(input("Введите порядок: "))
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(i, n):
        a[i][j] = j - i + 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end="\t ")
    print()

input()
