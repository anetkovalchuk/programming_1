n = int(input())
mas_1 = [int(el) for el in input().split()]
m = int(input())
mas_2 = [int(el) for el in input().split()]
mas_3 = []
for el in mas_1:
    if el not in mas_2:
        mas_3.append(el)
print(len(mas_3))
print(*mas_3)