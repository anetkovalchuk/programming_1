n = int(input())
mas = [float(el) for el in input().split()]
new_mas = []
for el in mas:
    if el > 0:
        new_mas.append(el)
if new_mas:
    average = sum(new_mas) / len(new_mas)
    print(f'{average:.2f}')
else:
    print('Not Found')