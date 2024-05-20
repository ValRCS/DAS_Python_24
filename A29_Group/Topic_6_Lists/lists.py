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
mixed_goods = [1, 2.99, "milk", True, None, "beer"] # list of mixed data types
# again mixed data types are not recommended but possible, sometimes it is convenient

# let's print the lists
print(empty_list)
print(prices)
print(products)
print(mixed_goods)

# let's find out how many of each item we have in the list
# we can use len() function
print(len(empty_list))
print(f"Number of prices: {len(prices)}")
print(f"Number of products: {len(products)}")
print(f"Number of mixed goods: {len(mixed_goods)}")

# Accessing Individual Items in a List
# first item in a list has index 0 - just like in strings
# first price
print(prices[0])
# first item in products
print(f"First product: {products[0]}")

# how about last product? - we have two approaches
# 1. we can use len() function to get the length of the list and then subtract 1
print(f"Last product: {products[len(products) - 1]}")
# 2. Better yet, we can use negative indexing
# -1 is the last item in the list, -2 is the second last item, etc.
print(f"Last product: {products[-1]}")

# all items are mutable - we can change them
# let's change 2nd price
prices[1] = 3.49
print(prices)

# if all items are numeric we can perform mathematical operations
# we can get a sum of all prices
total = sum(prices) # works for mix of ints and floats as well
print(f"Total price: {total}")
# then we can get the average price by using len() function
average = total / len(prices)
print(f"Average price: {average}")
# for more advanced statistics we can import statistics module - we will cover this later

# let's work with some beers
beers = ["Bauskas", "Aldaris", "Cēsu"]
# print current list
print(f"Beers: {beers}")

# let's add a new beer to the list
beers.append("Piebalgas") # IN PLACE METHOD - MODIFIES THE LIST!

# until now all our variables used primitive data types which are immutable - strings, integers, floats, booleans
# lists are mutable - we can change them

# let's print the list again
print(f"Beers: {beers}")

# we could store whatever we are going to add first
new_beer = "Valmiermuižas"
beers.append(new_beer)
print(f"Beers: {beers}")

# how about if we need to insert somewhere in the middle of the list?
# we can use insert() method
beers.insert(1, "Labietis") # IN PLACE METHOD - MODIFIES THE LIST!
# above 1 means it will insert before the second item in the list, 1 means second item
# the rest of the items will be shifted to the right
print(f"Beers: {beers}")
# so if I want to insert at very beginning I can use 0
beers.insert(0, "Aldaris") # so duplicate Aldaris will be inserted at the beginning
print(f"Beers: {beers}")
# how about using some big number for end
beers.insert(100_000, "Tērvetes") # it will insert at the end of the list, BUT append is preferred
print(f"Beers: {beers}")

# we also have an OUT OF PLACE approach using + and = operators
beers = beers + ["Užavas","Mežpils"] # this will create a new list and assign it to beers
print(f"Beers: {beers}")

# what happens if we try to append a list to a list?
beers.append(["Tērvetes", "Lāčplēsis"]) # it will add a list as a single item - not quite what we want
print(f"Beers: {beers}")

# so we do not want the last item - again we have two approaches to getting rid of it
# we could use pop() method - it will remove the last item and return it
last_item = beers.pop() # IN PLACE METHOD - MODIFIES THE LIST!
print(f"We just removed: {last_item}")
print(f"Beers: {beers}")

# another approach is to use slicing approach - OUT OF PLACE
beers = beers[:-1] # this will create a new list without the last item
print(f"Beers: {beers}")
# again we can use slicing to get multiple items at once
print(f"2nd and 3rd item {beers[1:3]}") # this will get 2nd and 3rd items
# slicing does not throw errors if we try to get more items than we have
print("Too many items", beers[2:100]) # this will get all items from 3rd to the end - as long as we have less than 100 

# returning to question of extending a list with another list - so called flattening
# OUT of place approach
# beers = beers + ["Tērvetes", "Lāčplēsis"] # this will create a new list and assign it to beers
# IN PLACE approach with extend
beers.extend(["Tērvetes", "Lāčplēsis"]) # this will add all items from the list to the end of the beers list
print(f"Beers: {beers}")
# how many beers do we have?
print(f"Number of beers: {len(beers)}")

