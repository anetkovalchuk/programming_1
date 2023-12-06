n = int(input())
binary = bin(n)[2:]
binary_to_xs = []

def binary_xs():
    for i in binary:
        if i == '1':
            binary_to_xs.append('SX')
        elif i == '0':
            binary_to_xs.append('S')

def delete_first_xs():
    for i in range(len(binary_to_xs)):
        if binary_to_xs[i] == "SX":
            binary_to_xs.pop(i)
            break  

binary_xs()
delete_first_xs()
print(*binary_to_xs, sep = '')

