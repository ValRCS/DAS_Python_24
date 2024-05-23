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

# now let's try changing something in another_tuple
try:
    another_tuple[0] = 5 
except TypeError as e:
    print(f"TypeError: {e}")

# if we do want to change then we have two options one is to change to list and then back to tuple
# of we could use slicing to create a new tuple
# let's try the first option

# first convert to list
list_from_tuple = list(another_tuple) # so type casting tuple to list will work with no fail
print(list_from_tuple)
# now change the value
list_from_tuple[0] = 5
print(list_from_tuple)
# now convert back to tuple
changed_tuple = tuple(list_from_tuple)
print(changed_tuple)

# second approach would be to use slicing of the tuple with the new value
# let's try that
new_tuple = (5,) + another_tuple[1:] # we need to add comma to make it a tuple
print(new_tuple)


# we only have two methods for tuples - count and index
# count - counts the number of times a value appears in the tuple
# index - returns the index of the first occurrence of a value

# let's try count
print(f"Count of 3 in tuple {tuple_with_nums}", tuple_with_nums.count(3))  # 1
print(f"Count of 10 in tuple {tuple_with_nums}", tuple_with_nums.count(10))  # 0    
# now how about finding a partial match in a tuple of strings - count would not work here
string_tuples = 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry','date','elderberry'
# we can count the number of times a string appears in the tuple
print(f"Count of 'apple' in tuple {string_tuples}", string_tuples.count('apple'))  # 2
# now how about counting how many times needle appears across all haystacks - here tuple is a haystack
needle = 'erry'
# count would give us 0
print(f"Count of 'erry' in tuple {string_tuples}", string_tuples.count(needle))  # 0
# we could use a simple loop
all_count = 0
for item in string_tuples:
    all_count += item.count(needle)
print(f"Count of 'erry' in tuple {string_tuples}", all_count)  # 3
# now try na
print(f"Count of 'na' in tuple {string_tuples}", string_tuples.count('na'))  # 0
all_count = 0
for item in string_tuples:
    all_count += item.count('na')
print(f"Count of 'na' in tuple {string_tuples}", all_count)  # 4
# let's make a function out of this counter
def count_needle_in_haystack_sequence(needle, haystack: tuple | list) -> int:
    """
    Count the number of times a needle appears in a sequence of strings
    :param needle: str - the string to search for
    :param haystack: tuple | list - the sequence of strings to search in
    :return: int - the number of times needle appears in the sequence
    """
    all_count = 0
    for item in haystack:
        all_count += item.count(needle)
    return all_count

# let's test it
print(f"Count of 'erry' in tuple {string_tuples}", count_needle_in_haystack_sequence('erry', string_tuples))  # 3

# now we can try index
print(f"Index of 3 in tuple {tuple_with_nums}", tuple_with_nums.index(3))  # 1 so 2nd element with index 1
# now cherry in string_tuples
print(f"Index of 'cherry' in tuple {string_tuples}", string_tuples.index('cherry'))  # 2 so 3rd element with index 2

# how could we find an index of all tuples with some value
# let's write a function that returns a tuple of indexes
def find_indexes_of_needle_in_haystack_sequence(needle, haystack: tuple | list) -> tuple:
    """
    Find the indexes of a needle in a sequence of strings
    :param needle: str - the string to search for
    :param haystack: tuple | list - the sequence of strings to search in
    :return: tuple - the indexes of the needle in the sequence
    """
    # indexes = tuple() # empty tuple
    # for index, item in enumerate(haystack):
    #     if needle in item:
    #         indexes += (index,) # here we are creating a new tuple with the index
    # return indexes
    # personally I would start with a list and then convert to tuple at the end
    indexes = [] # empty list
    for index, item in enumerate(haystack):
        if needle in item: # this is fuzzy search - if needle is in item works for full exact match as well
            indexes.append(index) # here we are adding the index to the list
    return tuple(indexes) # convert list to tuple

# let's test it
print(f"Indexes of 'erry' in tuple {string_tuples}", find_indexes_of_needle_in_haystack_sequence('erry', string_tuples))  # (2, 5, 7)

# cool thing with tuples is unpacking
# this leads to Pythonic way of swapping variables

a = 2001
b = 2024
print(a, b)
# how would you swap these values without unpacking?
# we would use a temporary variable
temp = a # so a is stored in temp
a = b # now we can overwrite a with b
b = temp # now we can overwrite b with temp
# and temp remains polluting the global namespace
print(a, b, temp)
# Python offers us a better way
a, b = b, a # we pack a tuple on the right and unpack it on the left
print("after unpacking", a, b)
# i could have saved this tuple
t = b, a
print(t)
# and unpacked it later
c, d = t
print(c, d)
# this works on as many variables as you want
a, b, c, d = 1, 2, 3, 4 # could be used for quick assignment
print("Before swapping", a, b, c, d)
# now let's swap all 4 
a, b, c, d = d, c, b, a
print("After swapping", a, b, c, d)

# we can use tuples as dictionary keys
valdis_a = 'Valdis', 'Berzins', 2001, 'Riga'
valdis_b = 'Valdis', 'Berzins', 1922, 'Carnikava'

# now those tuples can be used as keys
my_dict = {valdis_a: 'Valdis A', valdis_b: 'Valdis B'}
print(my_dict[valdis_a])
# full dictionary
print(my_dict)

# it should be noted that tuples are generally hashable

# exceptions are tuples with mutable elements inside those are not hashable
# those would be tuples with lists or dictionaries
# let's try to create a tuple with a list
try:
    tuple_with_list = (1, 2, 3, [4, 5, 6])
    print(tuple_with_list)
except TypeError as e:
    print(f"TypeError: {e}")

# so we have a list inside the tuple this means we can not use this tuple as a key in a dictionary

# now tuples are immutable but if you have mutable object inside, you can use IN PLACE methods on that object

# so this list is index 3 in our tuple
print(tuple_with_list[3])  # [4, 5, 6]
# i can append, extend, pop, remove, clear, sort, reverse on this list
tuple_with_list[3].append(7)
# print full tuple
print(tuple_with_list)
# so something to be aware of

# one more thing about tuples - they can be nested
nested_tuple = (1, 2, (3, 4, (5, 6))) # 3 levels of nesting
print(nested_tuple)
# how would I get to 5?
print(nested_tuple[2][2][0])  # 5

# when we get items from dictionaries we get list of tuples
# let's create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
# now let's get items
items = my_dict.items()
print(items)  # dict_items([('a', 1), ('b', 2), ('c', 3)])
# i could convert items to tuple or list if i want
items_tuple = tuple(items)
print(items_tuple)  # (('a', 1), ('b', 2), ('c', 3))


# some more learning resources on tuples stored as a tuple

learning_resources = (
    "https://docs.python.org/3/library/stdtypes.html#tuple",
    "https://realpython.com/python-tuples/",
    "https://www.w3schools.com/python/python_tuples.asp",
    "https://www.geeksforgeeks.org/tuples-in-python/",
    # Google developer Python course
    # TODO find Google info on tuples
)
# we can unpack this tuple to get the links in each row
print(*learning_resources, sep='\n') # * unpacks the tuple into individual elements to be printed
# above works on lists as well