def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    return int(str(n)[::-1])

def lucky_prime(n):
    reversed_n = reverse_number(n)
    return prime_number(n) and prime_number(reversed_n) and n != reversed_n

def finish_lucky_prime(k):
    count = 0
    num = 2  
    
    while count < k:
        if lucky_prime(num):
            count += 1
            if count == k:
                return num
        num += 1
    
    return -1  


k = int(input())

result = finish_lucky_prime(k)
print(result)