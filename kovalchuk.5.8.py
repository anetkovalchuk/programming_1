n = int(input())
num = list(map(int, input().split()))
min = 1000000
for el in num:
    if min > el:
        min = el
print(min)