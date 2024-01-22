# Exercise 3: Convert Decimal number to octal using print() output formatting

num = 92
quotient = 1
remainder = 0
rev_remainder = ""

while quotient != 0:
    remainder = num % 8
    quotient = num // 8
    num = quotient
    # print(remainder, quotient)
    rev_remainder += str(remainder)

print(rev_remainder[::-1])
