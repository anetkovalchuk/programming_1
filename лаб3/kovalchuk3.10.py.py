n = int(input())
i = 1
n1 = 0
while 10**(i-1) <= n:
    digit = 10**(i-1) // 10**(i-1)
    if digit // 2 == 0:
        digit = digit + 1
    else:
        digit = digit - 1
    i += 1
print(digit)



#if digit // 2:
   # digit += 1
#else:
 #   digit -= 1
#print(digit)