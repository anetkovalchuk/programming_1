a, b, c = [int(d) for d in input().split()]
if a == b == c:
    print(1)
if a == b != c or a == c != b or b == c != a:
    print(2)
if a != b and b != c and c != a:
    print(3)