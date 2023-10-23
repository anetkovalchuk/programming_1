n = int(input())
mas = [int(el) for el in input().split()]
new_mas = []

last_el = mas[n-1]
new_mas.append(last_el)
mas.pop(n-1)  
new_mas.extend(mas)
print(*new_mas)