n = int(input())
mas = [int(el) for el in input().split()]
new_mas = []
for el in mas:
    if el not in new_mas:
        new_mas.append(el)
print(*new_mas)
