def perms(n, current=[]):
    result = []
    if len(current) == n:
        result.append(current)
    else:
        for i in range(1, n + 1):
            if i not in current:
                result.extend(perms(n, current + [i]))
    return result

n = int(input())  
permutations = perms(n)
for p in permutations:
    print(' '.join(map(str, p)))






