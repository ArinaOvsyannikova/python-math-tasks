import math

input("Введите число a")
a = float(input())
if (1+math.cos(2*a) != 0)  and (1 + math.cos(4 * a) != 0):
    z1 = (math.sin(4 * a) / (1 + math.cos(4 * a))) * (math.cos(2 * a) / (1 + math.cos(2 * a)))
    print("z1=",z1)
else:
    print("значения z1 не существует")
if math.sin((3 / 2.0) * math.pi - a) != 0:
    z2 = math.cos((3 / 2.0) * math.pi - a) / math.sin((3 / 2.0) * math.pi - a)
    print("z2=",z2)
else:
    print("значения z2 не существует")
