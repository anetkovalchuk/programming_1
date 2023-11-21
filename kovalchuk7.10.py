d = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

m, k = map(int, input().split())
n = int(input(), m)

if n == 0:
    print('0')
else:
    r = ''
    while n > 0:
        r = d[n % k] + r
        n //= k
    print(r)