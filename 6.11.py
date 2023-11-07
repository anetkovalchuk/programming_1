password = input()
number_of_criteria = 0
special_characters = "!\"#$%&'()*+"
small_letter = False  
big_letter = False
numbers = False
characters = False

for i in password:
    if i.isalpha() and i.islower():
        small_letter = True 
    if i.isupper():
        big_letter = True
    if i.isdigit():
        numbers = True
    if i in special_characters:
        characters = True

if small_letter:
    number_of_criteria += 1
if big_letter:
    number_of_criteria += 1
if numbers:
    number_of_criteria += 1
if characters:
    number_of_criteria += 1
if len(password) >= 8:
    number_of_criteria += 1

print(number_of_criteria)