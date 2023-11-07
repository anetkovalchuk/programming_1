abc = input()
k = input()
k = int(k)
result = ''
for i in abc:
    i = ord(i)
    i = int(i)
    new_i = i - k
    if new_i < 65:
        new_i = 90 - (65 - new_i - 1)
    elif new_i > 90:
        new_i = 65 + (new_i - 91)
    new_i = chr(new_i)
    result += new_i 
print(result)