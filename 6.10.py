line = input()  
line_2 = ''
for i in line:
    if i.isalpha() and i.islower():
        line_2 += i * 2
    else:
        line_2 += i
print(line_2)