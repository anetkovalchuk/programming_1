import math
def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // gcd(a, b)

def nsk(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

n = int(input())
result = nsk(n)
print(result)