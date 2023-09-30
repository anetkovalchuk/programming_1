n = int(input())
parni = 0
while (n > 0):
    temp = n % 10
    if (temp % 2 == 0):
        parni += temp
    n = n // 10
if parni == 0:
    print('-1')
else:
    print(parni)