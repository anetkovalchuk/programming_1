def decimal_to_tridecimal(n):
    if n == 0:
        return "0"

    symbols = "0123456789ABC"

    tridecimal = ""
    while n > 0:
        remainder = n % 13
        tridecimal = symbols[remainder] + tridecimal
        n //= 13

    return tridecimal

n = int(input)
tridecimal_number = decimal_to_tridecimal(n)
print(tridecimal_number)
