def numbers_with_other_numbers(a, b):
    result = []
    for i in range(a, b + 1):
        num = [int(num) for num in str(i)]  
        if len(num) == len(set(num)): 
            result.append(i)  
    return result

a, b = map(int, input().split())
result = numbers_with_other_numbers(a, b)
print(*result)