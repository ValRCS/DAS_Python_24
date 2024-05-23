# Sets - kopas in Latvian
# Sets are unordered collections of unique elements
# Sets are mutable - we can add and remove elements
# So you can say sets are dynamic since they can change - somewhat different from lists or dictionaries
# Sets support so called set operations - union, intersection, difference, symmetric difference
# Sets are very efficient for membership testing - checking if an element is in a set - much faster than lists or tuples
# There are many set methods to be explored

# Main use cases for sets:
# - removing duplicates from a sequence
# - membership testing
# - mathematical set operations

# official set documentation: https://docs.python.org/3/library/stdtypes.html#set

# let's make a set from a string
char_set = set('abracadabra')
print("Unique characters in 'abracadabra':", char_set)
# note sets also use curly braces but they are not dictionaries
# note that running set multiple times will give different results as sets are unordered
# there are ordered set data types in Python but they are not built-in, some languages have ordered sets by default
# the reason for having unordered sets is that they are more efficient for membership testing - O(1) time complexity

# now we can use this set if any letter is in this set
print("a in set?", 'a' in char_set)  # True # O(1) time complexity - Faster than O(n) time complexity for lists/tuples
print("z in set?", 'z' in char_set)  # False

# so one of the takeways from this lecture 
# if we expect to be checking if an element is in a collection many times - use a set
# if we only have to check once then there is no point in converting a list to a set just for that

# now how about gettin a string out of set?
print(str(char_set))  #  - not very useful
# we could use join method to get a string out of set
print(''.join(char_set))  # all letters but not sorted
# we could also first use sorted function to sort the set
print(''.join(sorted(char_set)))  # sorted letters

# we can use set on any iterable
# let's try it on list of food words
food_list = ['apple', 'banana', 'cherry', 
             'apple', 'banana', 'cherry', 
             'apple', 'banana', 'cherry',
             'date', 'elderberry']
food_set = set(food_list)
print("Unique food words:", food_set) # again not lack of order
# if we just want a tuple or list we can simply use tuple or list functions
food_tuple = tuple(food_set)
print("Unique food words as tuple:", food_tuple)
food_list = list(food_set)
print("Unique food words as list:", food_list)
# or we could use sorted function
sorted_unique_food_list = sorted(food_set) # if I wanted a tuple I would add tuple() around sorted()
print("Sorted unique food words as list:", sorted_unique_food_list)
