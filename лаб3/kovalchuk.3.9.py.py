n = int(input())
i = 0
num = 1
while i < n:
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        i += 1
        print(num, end=" ")
    num +=1