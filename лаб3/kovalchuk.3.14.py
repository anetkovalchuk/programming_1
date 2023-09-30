n = int(input())
fac = 1
for i in range(1,n+1,):
    fac = fac * i
count = 0
while fac > 0:
    fac //= 10
    count += 1
print(count)