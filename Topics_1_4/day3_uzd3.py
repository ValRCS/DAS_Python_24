a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))

# Sort the numbers using nested if-elif-else based on the description
# this is DESCENDING (usually we do ASCENDING just switch the equalities
if a >= b >= c:  # a is the largest
    print(a, b, c)  # a, b, c
elif a >= c >= b:
    print(a, c, b)  # a, c, b
elif b >= a >= c:
    print(b, a, c)  # b, a, c
elif b >= c >= a:
    print(b, c, a)  # b, c, a
elif c >= a >= b:
    print(c, a, b)  # c, a, b
else: # could write elif c >= b >= a
    print(c, b, a)  # c, b, a


# Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām

# Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.