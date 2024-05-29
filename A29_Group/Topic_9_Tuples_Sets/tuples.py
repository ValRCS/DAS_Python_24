# Python tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Docs: https://docs.python.org/3/library/stdtypes.html#tuples
# Tuple in Latvian: "kortežs"
# simply think of them as read-only lists

# some properties of tuples
# - Tuples are immutable - we do not change the values of the tuple
# - Tuples are ordered - we can access elements by index

# Usage of tuples
# - Tuples are used to store multiple items in a single variable
# - Tuples are faster than lists - not much but still
# - Tuples are used when the data cannot change
# - Tuples can be dictionary keys
# - Tuples can be used for packing and unpacking

# Philosophically
# Tuples - for heterogeneous data - any type of data
# Lists - for homogeneous data - same type of data - e.g. list of numbers

# Tuple creation
# using ()
# using tuple() function

my_tuple = (1, 2, 3, 4, 5)
# parentheses are optional for most cases
also_my_tuple = 1, 2, 3, 4, 5
print(my_tuple)
print(also_my_tuple)
# we can store any data types in a tuple
mixed_tuple = (10, "Valdis", 3.14, None, True, {'a':50, 'b':70},[1, 2, 3])
print(mixed_tuple)

# now let's explore indexing
print(mixed_tuple[0]) # 10
# last item
print(mixed_tuple[-1]) # [1, 2, 3]
# second to last item
print(mixed_tuple[-2]) # {'a':50, 'b':70}
# value for key b from the dictionary
print(mixed_tuple[-2]['b']) # 70, get would also work

# slicing also works
# let's use my_tuple
print(my_tuple[1:3]) # (2, 3) # this is a new tuple, original tuple is not modified
print(my_tuple[:3]) # (1, 2, 3) # this is a new tuple, original tuple is not modified
print(my_tuple[2:]) # (3, 4, 5) # this is a new tuple, original tuple is not modified

# how do we reverse a tuple?
reversed_tuple = my_tuple[::-1] # i can not reverse the original tuple
print(reversed_tuple)
print(my_tuple)
# if I do not need original tuple I can reassign
my_tuple = my_tuple[::-1] # original tuple is lost forever... :)
print(my_tuple)

# if I want to change some value in a tuple
# then one approach is simply to convert tuple to a list
my_list = list(my_tuple)
print(my_list)
# let's change 2nd element to 9000
my_list[1] = 9000
# let's append a new element as well
my_list.append(1000)
print(my_list)
# now I can reconvert list to a tuple
my_tuple = tuple(my_list) # here my_tuple is a new tuple, old one is lost
print(my_tuple)
# I could also use tuple concatenation
my_tuple = my_tuple + (1001, 1002)
print(my_tuple)
# so how would I concatenate tuple with single element?
my_tuple += (1001,) # notice the comma # without comma it would be a number
print(my_tuple)

# normal iterable functions work such as len, sum, min, max
print(f"Lenght of my_tuple is {len(my_tuple)}")
print(f"Sum of my_tuple is {sum(my_tuple)}")
print(f"Min of my_tuple is {min(my_tuple)}")
print(f"Max of my_tuple is {max(my_tuple)}")

# of course for sum, min, max all elements should be of the same type

# we can loop through our tuple
for item in mixed_tuple:
    print(item)

# tuples only have two methods
# count - count of a value
# index - index of a value
print(my_tuple.count(1001))
# second is index
# index of first occurence of value
print(my_tuple.index(1001))

# so how could I create a function to return a tuple of all indexes of a value?
def all_indexes(my_tuple, needle):
    indexes = []
    for i in range(len(my_tuple)):
        if my_tuple[i] == needle:
            indexes.append(i)
    return tuple(indexes)

print(all_indexes(my_tuple, 1001))

# let's create this same function using index method
def all_indexes_v2(my_tuple, needle):
    indexes = []
    i = 0 # we start looking at index 0
    try:
        while True:
            i = my_tuple.index(needle, i)
            indexes.append(i)
            i += 1 # I will use next position to find next index
    except ValueError:
        return tuple(indexes)

print(all_indexes_v2(my_tuple, 1001))

# we can use tuples to pack and unpack values
# packing
my_packed_tuple = 1, 2, 3, 4, 5
print(my_packed_tuple)
# unpacking
a, b, c, d, e = my_packed_tuple # so 5 variables will be created
print(a, b, c, d, e)
# so I can use this to assign multiple variables at once
a, b, c, d = 10, 20, 30, 40

# from this we can create a swap function without using a temporary variable
new_year = 2024
old_year = 2001
print(new_year, old_year)
# without tuple unpacking I would need a temporary variable
temp = new_year
new_year = old_year
old_year = temp
print(new_year, old_year)
# with Python we can do this in one line
new_year, old_year = old_year, new_year # we pack from right and unpack from left
print(new_year, old_year)

# we can swap multiple variables at once
a, b, c, d = d, c, b, a
print(a, b, c, d)

# tuples can be used as dictionary keys
person1 = ('Valdis', 'Zibens', 50)
person2 = ('Valdis', 'Saulespurens', 50)
person3 = ('Līga', 'Pērkona', 40)
# now we will store some info about these people
people = {}
people[person1] = {'city':'Rīga', 'country':'Latvia'}
people[person2] = {'city':'Jūrmala', 'country':'Latvia'}
people[person3] = {'city':'Rīga', 'country':'Latvia'}
print(people)

# so let's find the city for Valdis Zibens
print(people[person1]['city'])

# also we often get list of tuples
# one example is dictionary items method
# let's get people items
people_items = list(people.items())
print(people_items)

# let's use simpler example 
text = "AĀBCČDEĒ"
text_dict = {k:ord(k) for k in text}
print(text_dict)
# compare to list of tuples
text_items = list(text_dict.items())
print(text_items)
# let's remove last one
text_items.pop()
# now make a new dictionary from list of tuples
new_text_dict = dict(text_items)
print(new_text_dict)
# again dictionary would be preferable for access by key
# list of tuples would be used to create a new dictionary or for iteration

# there is one caveat with tuples
# if tuple contains mutable elements such as lists or dictionaries
# tuple can not be used as a dictionary key
# second we can mutate the mutable elements of a tuple using IN-PLACE methods