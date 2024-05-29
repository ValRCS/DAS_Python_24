# Sets - Kopas Latviski
# Sets are unordered collections of unique elements. 
# We can construct them by using the set() function.
# Set properties:
# Sets are unordered - ! no indexing !
# Sets do not allow duplicates - all items are unique
# Sets are mutable - we can add and remove items

# Usage of sets
# - remove duplicates from a lists, tuples, etc
# - check for membership - quicker than lists or tuples for large collections
# - set operations - union, intersection, difference, etc

# Documentation: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

# Set creation
# using {}
# using set() function

no_duplicates = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5,7,8,900, 900, 900}
print(no_duplicates) # Note that ORDER is NOT GUARANTEED
# there is such a thing as ordered set but it is slower
# so no such thing as free lunch in computing

# note - we've run out of parenthesis for set creation
# so we are using same curly braces as for dictionaries
# the difference is that dictionaries have key:value pairs
# sets have just values 

# second approach to set creation is to use set() function
# set function takes iterable as an argument
# so we can pass a list, tuple, string, etc
# let's try with a string
char_set = set('abracadabra')
print(char_set) # - note that duplicates are removed

# so if you need specific order for usage simply use sorted() to convert to list
char_list = sorted(char_set)
print(char_list)

# similarly with numbers in no_duplicates set
num_list = sorted(no_duplicates)
print(num_list)

# so one workflow to remove duplicates would be simply to convert to set and back to list
food_list = ['apple', 'banana', 'apple', 'banana', 'cherry', 'apple', 'cherry', 'date', 'apple']
print(food_list)
food_set = set(food_list)
print(food_set)
food_list_unique = list(food_set) # replace list with sorted() if you need specific order
print(food_list_unique)
# sorted
food_list_unique = sorted(food_set)
print(food_list_unique)

# second