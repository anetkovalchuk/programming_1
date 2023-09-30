n = int(input()) 
fac = 1
for i in range(1, 2001): 
    fac = fac * i 
    if (fac == n): 
        print(i) 
        break