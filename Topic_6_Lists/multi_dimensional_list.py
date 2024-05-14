# we can create multi-dimensional lists with list comprehension or with loops
# let's create a 2d list of multiplication table
# let's use for loop
multiplication_table = []
for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i*j)
    multiplication_table.append(row)

# print(multiplication_table)
for row in multiplication_table:
    print(row)
# a trick to print 2d lists in a more readable way
print(*multiplication_table, sep='\n') # with * we unpack the list into separate arguments

# so If I have two dimensional list I can access elements with two indexes
print(multiplication_table[2][5]) # 3rd row 6th column because both indexes start from 0

# we can slice 2d lists as well
print(multiplication_table[2][1:5]) # 3rd row 2nd to 5th column

print(multiplication_table[3])
