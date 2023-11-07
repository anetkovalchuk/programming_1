n = int(input())
num = [int(input()) for _ in range(n)]
for x in num:
    if x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')