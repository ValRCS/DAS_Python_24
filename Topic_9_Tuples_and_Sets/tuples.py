# Python Tuples (a, b, c, d, e) - Latviski - korteži, nemaināmi saraksti
# some properties of tuples
# Immutable - we don't change the values of a tuple itself
# Usage - pass data around, return multiple values from a function
# Tuples are faster than lists
# Tuples are used as dictionary keys - tuples are generally hashable
# Tuples uses for packing and unpacking
# Tuples are indexed, ordered, and iterable
# Tuples have their own methods, but fewer than lists
# Tuples can be nested just like lists
# Philosophically - Tuples are for heterogeneous data (different data types)
#  lists are best for homogeneous data - same type of data
# Python lets us use either for either, but it's a good practice to use them as intended
# Documentation: https://docs.python.org/3/library/stdtypes.html#tuple

# let's create a tuple
tuple_with_nums = (1, 2, 3, 4, 5) # note regular parentheses
# parenthesis are actually optional - works for creating most tuples when it is clear
another_tuple = 2, 10, 3.14, 'hello', 'DAS'  # note different data types
# print
print(tuple_with_nums)
print(another_tuple)

# normal indexing works
print(tuple_with_nums[0])  # 1
print(another_tuple[3])  # hello is 4th element with index 3
# negative indexing works as well
print(tuple_with_nums[-1])  # 5

# similarly slicing works
print(tuple_with_nums[1:4])  # (2, 3, 4)
print(another_tuple[1:])  # (10, 3.14, 'hello', 'DAS') - all elements from index 1
# similarly we can reverse a tuple
print(tuple_with_nums[::-1])  # (5, 4, 3, 2, 1)

# again tuples are immutable - we can't change the values so we are creating new tuples with slicing
# so I can store the new tuple in the same variable
tuple_with_nums = tuple_with_nums[1:4] # this would be (2, 3, 4) I owerwrite the old tuple
print(tuple_with_nums)
# similarly i could store reverse in the same or new variable
tuple_reversed = tuple_with_nums[::-1]  # (4, 3, 2)
print(tuple_reversed)

# we have usual operations such as len, min, max, sum - where appropriate for data type
print(len(tuple_with_nums))  # 3
print(f"min of tuple {tuple_with_nums}", min(tuple_reversed))  # 2
print(f"max of tuple {tuple_reversed}", max(tuple_reversed))  # 4
print(f"sum of tuple {tuple_reversed}", sum(tuple_reversed))  # 9

# now for mixed types we can only get len
print(f"Length of another tuple {another_tuple}", len(another_tuple))  # 5
# sum would not work as it is not possible to sum different types
try:
    print(sum(another_tuple))
except TypeError as e:
    print(f"TypeError: {e}")

# we can also use in and not in operators for membership testing
print("is 2 found in our tuple?", 2 in tuple_with_nums)  # True
print("is 10 found in our tuple?", 10 in tuple_with_nums)  # False
# membership testing is linear for tuples meaning we have to go through all elements just like lists

# we can also use for loop to iterate over tuples
for element in another_tuple: # now element is just a variable name could be anything
    print(element)