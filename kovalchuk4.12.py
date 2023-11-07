num = []
while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)
total_sum = 0
for n in num:
    if n % 2 == 0:
        total_sum += n
print(total_sum)