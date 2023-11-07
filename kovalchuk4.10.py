n = int(input())

if n == 1:
    total_sum = 0
    for num in range(100, 1000):
        if num % 2 == 0 and (num // 10) % 2 == 0 and (num // 100) % 2 == 0:
            total_sum += num
    print(total_sum)

elif n == 2:
    count = 0
    for num in range(100, 1000):
        hundreds = num // 100
        tens = (num // 10) % 10
        ones = num % 10
        if hundreds < tens < ones:
            count += 1
    print(count)

elif n == 3:
    total_sum2 = 0
    for num in range(100, 1000):
        if num % 2 != 0 and (num // 10) % 2 != 0 and (num // 100) % 2 != 0:
            total_sum2 += num
    print(total_sum2)

elif n == 4:
    count2 = 0
    for num in range(100, 1000):
        hundreds = num // 100
        tens = (num // 10) % 10
        ones = num % 10
        if hundreds > tens > ones:
            count2 += 1
    print(count2)

elif n == 5:
    total_sum3 = 0
    for num in range(100, 1000):
        hundreds = num // 100
        tens = (num // 10) % 10
        ones = num % 10
        if (hundreds**3) + (tens**3) + (ones**3) == num:
            total_sum3 += num
    print(total_sum3)

elif n == 6:
    count3 = 0
    for num in range(100, 1000):
        hundreds = num // 100
        tens = (num // 10) % 10
        ones = num % 10
        if hundreds != tens and tens != ones and ones != hundreds:
            count3 += 1
    print(count3)