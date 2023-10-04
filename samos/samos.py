n =  int(input())
product = 1
for i in range(1,n+1):
    if i % 8 == 0:
        product = product * i
print(product)