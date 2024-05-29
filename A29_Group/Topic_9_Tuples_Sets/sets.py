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

# second major useage is for membership testing
# let's see if we have some specific food in our food list
print("Appple in food set?", 'apple' in food_set)
bad_needle = "pineapple"
print(f"{bad_needle} in food set?", bad_needle in food_set)
# this check will be much faster than using list or tuple
# for lists and tuples in operator is linear O(n) operation
# for sets it is O(1) operation
# in some ways it is similar to check for key in dictionary

# in practice this means that if we expect many membership checks
# then it would make sense to convert our list to a set

# note that there is not much point in converting list to set if we are only going to do
# a one or two membership checks
# because creating a set is also a linear operation O(n)

# in programming we can trade space for time and vice versa

# let's see an example where set membership would beat list membership
big_list = list(range(1000000))
big_set = set(big_list)
print(999999 in big_list) # True - but this is slow
print(999999 in big_set) # True - very very fast

# how to convert string set to string
food_string = " ".join(food_set)
print(food_string)
# I could also use sorted() if I need specific order
food_string = "<-|->".join(sorted(food_set))
print(food_string)

# now let's move onto set operations
# union, intersection, difference, symmetric difference

# at the same time we will explore more set methods
# add, remove, discard, pop, clear, update, intersection_update, difference_update, symmetric_difference_update

number_set = set(range(5))
print(number_set)
number_set.add(5) # single element add
print(number_set)
# how to add more than one element?
# update method
number_set.update({3,2, 6, 7, 8, 9, 10}) # duplicates will be ignored
print(number_set)
# i can remove an element
# let's remove 0
number_set.remove(0) # if element is not found we will get an error
print(number_set)
# so might be an idea to wrap in try
try:
    number_set.remove(0)
except KeyError as e:
    print("Key Error", e)

#alternative would be to use if statement
if 0 in number_set: # for sets this check is O(1) operation very quick
    number_set.remove(0)

# let's explore union
n_3_7 = set(range(3,8))
n_5_9 = set(range(5,10))
print(n_3_7)
print(n_5_9)

# union - sapludinājums?
# union means all elements from both sets
n_3_9 = n_3_7.union(n_5_9)
print(n_3_9)
# we have a shorter way to do union using | operator
n_3_9_also = n_3_7 | n_5_9
print(n_3_9_also)
# check that sets are the same?
print(n_3_9 == n_3_9_also)
# there is a difference between union and | operator
# union can be given any iterable
# | requires both operands to be sets
# so with union I coul give range or list or tuple
# with | I have to give two sets
another_set = number_set.union("Valdis150")
print(another_set) # note that 1 is not the same as "1"
# if I needed the same result with | operator I would have to convert string to set

# now let's explore intersection - šķēlums?
# intersection means common elements between two sets
n_5_7 = n_3_7.intersection(n_5_9)
print(n_5_7)
# there is a shorter way to do intersection using & operator
n_5_7_also = n_3_7 & n_5_9
print(n_5_7_also)
# same restrictions as with union
# intersection can be given any iterable
# & requires both operands to be sets

# there is also difference method
# difference means elements in first set that are not in second set
n_3_4 = n_3_7.difference(n_5_9)
print(n_3_4)
# there is a shorter way to do difference using - operator
n_3_4_also = n_3_7 - n_5_9
print(n_3_4_also)
# again - requires both operands to be sets, else - would be used for subtraction

# so set difference is not symmetric
n_8_9 = n_5_9.difference(n_3_7)
print(n_8_9)
n_8_9_also = n_5_9 - n_3_7
print(n_8_9_also)

# then there is symmetric difference
# this is for elements that are in one set or the other but NOT IN BOTH
n_3_4_8_9 = n_3_7.symmetric_difference(n_5_9)
print(n_3_4_8_9)
# there is a shorter way to do symmetric difference using ^ operator
# there is some analogy with XOR operator for bits
n_3_4_8_9_also = n_3_7 ^ n_5_9
print(n_3_4_8_9_also)

# let's explore more set methods
# we might want to know if one set is subset of another

# is n_3_7 subset of n_5_9?
print("is n_3_7 subset of n_5_9?", n_3_7.issubset(n_5_9))
# how 3_7 being subset of number_set?
print("is n_3_7 subset of number_set?", n_3_7.issubset(number_set))
# there is a shorter way to check subset using <= operator
print("is n_3_7 subset of number_set?", n_3_7 <= number_set)
# we even have strict subset method using < operator
print("is n_3_7 strict subset of number_set?", n_3_7 < number_set)
# how about itself?
print("is n_3_7 subset of n_3_7?", n_3_7.issubset(n_3_7))
# with strict
print("is n_3_7 strict subset of n_3_7?", n_3_7 < n_3_7)

# we can also do the same for superset
# this means that all elements of other set are in this set
print("is number_set superset of n_3_7?", number_set.issuperset(n_3_7))
# again we have shorter version
print("is number_set superset of n_3_7?", number_set >= n_3_7)
# strict superset
print("is number_set strict superset of n_3_7?", number_set > n_3_7)

# let's explore more set methods
# pop, clear, discard
# pop is for removing random element
print(number_set)
print(number_set.pop()) # this will remove one random? element and return it
# I believe randomness stems from the fact that set is unordered
print(number_set)

# discard is for removing specific element
number_set.discard(5) 
# discard is just like remove but does not raise error if element is not found
print(number_set)

# clear is for removing all elements
number_set.clear()
print(number_set) # set() - empty set, not {} - that would be empty dictionary
# again we can start updating our set
number_set.update(range(5))
print(number_set)

# so we can use set operations to compare lists first converting them to sets