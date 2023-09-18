n = int(input())
a = n // 100
c = n % 10
if a > c:
    print(a)
if c > a:
    print(c)
if a == c:
    print('=')
