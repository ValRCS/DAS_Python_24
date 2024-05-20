# Let's start why do we need lists at all
# imagine I want to store some data for my shopping list
# I could do it like this:
product_1 = "apple"
product_2 = "banana"
product_3 = "milk"
product_4 = "bread"
# this could work for a few items but what about 100 items?
# what about 1 million items?

# as a solution Python offers a data structure called list (array in other languages)
# list is a collection of items that are ordered in a specific order and changeable
# list properties:
# - ordered - means we will have indexes for each item
# - mutable - means we can change the items in the list
# - can contain any data type - strings, integers, floats, other lists, booleans, etc.
# - can be nested - list inside a list inside a list .. and so on
# - can contain duplicates - we can have the same item multiple times in the list
# - can be empty - we can create an empty list
# - dynamic - we can add or remove items from the list

# some good practices:
# - use meaningful names for lists - such as shopping_list instead of list_1
# - do not use list as a name for a list - it is a reserved word in Python
# - if possible use plural names for lists - such as products instead of product
# - try to store similar data in a list - such as all products in a shopping list
# - this means try to store all numbers in a list, all strings in a list, etc.
# - there are exceptions to this rule - such as storing all data in a list

# How do we create a list?
# we can use square brackets [] or use list() function
# most often we use square brackets

empty_list = [] # we can add items later
prices = [1.99, 2.99, 3.99, 4.99] # list of floats
products = ["apple", "banana", "milk", "bread"] # list of strings

# let's print the lists
print(empty_list)
print(prices)
print(products)

# let's find out how many of each item we have in the list
# we can use len() function
print(len(empty_list))
print(f"Number of prices: {len(prices)}")
print(f"Number of products: {len(products)}")