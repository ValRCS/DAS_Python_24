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

# now let's explore differences between set() and using {} to create a set
# with set() we can create an empty set
# set takes any iterable as an argument
empty_set = set()
print("Empty set:", empty_set)
# with {} we can create an empty dictionary
some_number_set = {1, 2, 3, 5,1, 0, -5, 1,3,3,1,2,3}
print("Some number set:", some_number_set)
# again if I want the uniques ordered I would use sorted() to get list or tuple
# how about using set() on some iterable?
some_number_list = [1, 2, 3, 5,1, 0, -5, 1,3,3,1,2,3]
some_number_set = set(some_number_list)
print("Some number set:", some_number_set)

# we can update our sets
# let's start with an empty set
empty_set = set()
# let's add some elements
empty_set.update(some_number_list)
print("Empty set after update:", empty_set)
# let's add some more elements
empty_set.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # so update takes any iterable, set/list/tuple
print("Empty set after another update:", empty_set)
# we can also remove elements
empty_set.remove(1)
print("Empty set after removing 1:", empty_set)
# i could add different date types to set
empty_set.add('Valdis') # so add method adds a single element
print("Empty set after adding Valdis:", empty_set)

# now let's do some set operations 
# set operations are based on mathematical set operations
# union, intersection, difference, symmetric difference
# let's start with two sets

numbers = set(range(12))
print("Numbers set:", numbers)
n3_7 = set(range(3, 8))
print("Numbers 3 to 7 set:", n3_7)
n5_9 = set(range(5, 10))
print("Numbers 5 to 9 set:", n5_9)

# let's start with a union
# union is all elements from both sets - no duplicates all unique elements
n3_9 = n3_7.union(n5_9)
print("Union of 3-7 and 5-9:", n3_9)
# Python offers also a shortcut for union
n3_9_also = n3_7 | n5_9 # so | between sets is a union
print("Union of 3-7 and 5-9 also:", n3_9_also)
# I believe union method let us use any iterable while | operator is only for sets
another_set = n3_7.union(range(100, 105)) # could use list or tuple here as well
print("Union of 3-7 and 100-104:", another_set)
# let's try with |
try:
    another_set = n3_7 | range(100, 105) # so | operator is only for sets
    print("Union of 3-7 and 100-104:", another_set)
except TypeError as e:
    print("We got a TypeError:", e)

# we can union with multiple sets
n3_9_12 = n3_9.union(numbers).union(range(16, 18)) # so union is associative
print("Union of 3-9, all numbers and 16-18:", n3_9_12)
# could use | if there are only sets
n3_9_12_also = n3_9 | numbers | set(range(16, 18)) # note I had to convert range to set
print("Union of 3-9, all numbers and 16-18 also:", n3_9_12_also)


# next up is intersection
# so Intersection is all elements that are in BOTH sets
n5_7 = n5_9.intersection(n3_7)
print("Intersection of 3-7 and 5-9:", n5_7)
# Python offers also a shortcut for intersection
n5_7_also = n5_9 & n3_7 # so & between sets is an intersection
print("Intersection of 3-7 and 5-9 also:", n5_7_also)
# similarly to union we can use any iterable with intersection
# for & operator we need sets

# so let's try to find common interests for two people
person1_interests = {'Python', 'Cycling', 'Cooking', 'Reading', 'Running'}
person2_interests = {'Python', 'Cycling', 'Cooking', 'Dancing', 'Singing'}
common_interests = person1_interests.intersection(person2_interests)
print("Common interests:", common_interests) # again original order is not preserved

# one gotcha with intersection is that it will return an empty set if there are no common elements
# with union we can start with empty set and build up

# with intersection we need at least one common element
empty_set = set()
empty_intersection = person1_interests & person2_interests & empty_set # so empty set ruins everything in intersection
print("Empty intersection:", empty_intersection)

# next up is difference
# difference is all elements that are in the first set but not in the second set
n3_4 = n3_7.difference(n5_9)
print("Difference of 3-7 and 5-9:", n3_4)
# again we have a shorter way of writing this using -
n3_4_also = n3_7 - n5_9 # so - between sets is a difference
# again - will work if these are sets! if those are numbers we would get arithmetic difference
print("Difference of 3-7 and 5-9 also:", n3_4_also)

# so difference is not symmetric
# let's try other way around
n8_9 = n5_9.difference(n3_7)
print("Difference of 5-9 and 3-7:", n8_9)

# there there is symmetric difference
# symmetric difference is all elements that are in one set or the other but not in both sets
# let's try it for our n3_7 and n5_9
n3_4_8_9 = n3_7.symmetric_difference(n5_9)
print("Symmetric difference of 3-7 and 5-9:", n3_4_8_9)
# let's try it for our persons
unique_interests = person1_interests.symmetric_difference(person2_interests)
# so we get all interests that are unique to each person
print("Unique interests:", unique_interests)
# there is also a shortcut for symmetric difference ^
unique_interests_also = person1_interests ^ person2_interests # so ^ between sets is a symmetric difference
print("Unique interests also:", unique_interests_also)

# we can also check if a set is a subset of another set
# let's try it with our numbers
print("is 3-7 subset of 0-11 ?",  n3_7.issubset(numbers))
print("is 3-9-12 subset of 0-11 ?",  n3_9_12.issubset(numbers))
# again we have a shorter way of writing this using <=
print("is 3-7 subset of 0-11 ?",  n3_7 <= numbers)
# we also have strong subset check
print("is 3-7 strict subset of 0-11 ?",  n3_7 < numbers)
# difference is that strict subset does not allow for equality
print("is 3-7 strict subset of 3-7 ?",  n3_7 < n3_7)

# then we have equivalent for superset
print("is 0-11 superset of 3-7 ?",  numbers.issuperset(n3_7))
# similarly we have syntactic sugar for superset
print("is 0-11 superset of 3-7 ?",  numbers >= n3_7)
# and strict superset
print("is 0-11 strict superset of 3-7 ?",  numbers > n3_7)

# let's explore a few more methods
# first we can loop through our set members

for number in numbers:
    print(number)

# we can also remove elements from a set
# let's remove 0 from numbers
numbers.remove(0)
print("Numbers after removing 0:", numbers)
# if I try it again I will get a KeyError
try:
    numbers.remove(0)
except KeyError as e:
    print("We got a KeyError:", e)

# we already saw update for iterable adding to set and also add for single element

# we also have pop method
# pop will remove and return an arbitrary element from the set
# let's try it with our numbers
print("Popped element from numbers:", numbers.pop())
print("Numbers after popping one element:", numbers)
# if we try to pop from an empty set we will get a KeyError

# we can also clear a set
numbers.clear()
print("Numbers after clearing:", numbers)
# and we could start adding again to our numbers set

# let's create a set of urls containing resources about sets
learning_set = {
    'https://docs.python.org/3/library/stdtypes.html#set',
    'https://realpython.com/python-sets/',
    # the rest are not so authoritative but still useful
    'https://www.w3schools.com/python/python_sets.asp',
    'https://www.programiz.com/python-programming/set',
    'https://www.geeksforgeeks.org/sets-in-python/',
    'https://www.learnpython.org/en/Sets',
    'https://www.tutorialspoint.com/python/python_sets.htm',
    'https://www.datacamp.com/community/tutorials/sets-in-python',
    # we could add some duplicates here and they will be ignored
    'https://www.datacamp.com/community/tutorials/sets-in-python',
    'https://www.datacamp.com/community/tutorials/sets-in-python',


}
# let's print all learning resources
for url in learning_set:
    print(url)
