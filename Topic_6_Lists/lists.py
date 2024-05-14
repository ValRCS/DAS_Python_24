# let's start why we need a list or some other sequence type
# imagine we are keeping track of some prices
cena1 = 1.99
cena2 = 2.99
cena3 = 3.50
cena4 = 4.99
# this approach is not very scalable, what if we have 100 prices?
# how about a million or billion?

# Python offers us a list - a sequence type
# list is a collection of items in a particular order
# list properties:
# - ordered
# - mutable - meaning we can change the elements
# - can contain duplicates
# - can contain different types of elements (strings, integers, floats, Booleans, other lists, etc.)
# - can be nested (a list inside a list and so on)
# - dynamic - meaning we can add or remove elements

# again we can store different types of elements in a list
# best practice is to use a descriptive name for the list
# also best to use it for similar items

# creating a list
# we use square brackets [] to define a list or list()

empty_list = [] # we can add to it later
prices = [1.99, 2.99, 3.50, 4.99] # already populated with some values
# very typical to use English plural form for the list name such as prices, names, etc.

# printing everything
print("Empty list", empty_list)
print(f"All prices {prices}")

# how about length of the list
print(f"Length of prices list is {len(prices)}")

# how do I access the first element of the list?
# we use the index of the element which starts at 0
# so to access the first element we use index 0
print(f"First price is {prices[0]}")
# how about the last element?
# we could use the length of the list - 1 but is not Pythonic
# instead we use -1 index which is Pythonic approach
print(f"Last price is {prices[-1]}")