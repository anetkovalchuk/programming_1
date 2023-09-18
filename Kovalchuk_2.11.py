n = int(input())
if n % 2 == 0 and not (n < 0 and n % 3 == 0):
    print("YES")
elif (n < 0 and n % 3 == 0) and not n % 2 == 0:
    print("YES")
else:
    print("NO")
 