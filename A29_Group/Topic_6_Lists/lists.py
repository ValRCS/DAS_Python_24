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

# let's get first 3 beers
first_3_beers = beers[:3] # OUT OF PLACE by slicing - at the moment of slicing we create a new list
print(f"First 3 beers: {first_3_beers}")
print(f"Last 3 beers: {beers[-3:]}") # OUT OF PLACE by slicing

# let's sort the list - again we have TWO approaches
# OUT OF PLACE approach 
# why out of place first? - because it does not modify the original list
sorted_beers = sorted(beers) # this will create a new sorted list
print(f"Sorted beers: {sorted_beers}")
# original list is still the same
print(f"OG Beers: {beers}")
# IN PLACE approach
beers.sort() # this will modify the original list - so original list will be sorted and original order lost
print(f"Sorted original beers: {beers}")

# let's compare contents of two lists
# we can use == operator
# it will compare each item in the list one by one and will return True if all items are the same in the same order
# and False otherwise
print(f"Our beer lists have same contents: {beers == sorted_beers}")
# however those lists are completely different objects
# for object comparison we can use is operator
print(f"Beers is same object as sorted beers?: {beers is sorted_beers}")

# for mutable objects = will create a new reference to the same object! not a copy!
beer_alias = beers # not a copy just a new reference to the same object

# if we want a copy we can use copy() method
beer_copy = beers.copy() # OUT OF PLACE method - creates a new list WITHOUT modifying the original list

# let's remove Aldaris from our beer_alias list
beer_alias.remove("Aldaris") # IN PLACE method - modifies the list, by removing one item
# now let's see all our beer variables
print(f"Beers: {beers}")
print(f"Beer alias: {beer_alias}")
# copy is unaffacted by the change
print(f"Beer copy: {beer_copy}")
# let's remove first Aldaris from the copy as well
beer_copy.remove("Aldaris") # IN PLACE method - modifies the list, by removing one item

# now let's compare again beer with beer_alias and beer_copy
print(f"Beers is same object as beer_alias?: {beers is beer_alias}") # so contents are same
print(f"Beers is same object as beer_copy?: {beers is beer_copy}")
print(f"Beer alias has same contents as beer_copy?: {beers == beer_copy}")

# let's see how many Aldaris beers we have in the list
print(f"Number of Aldaris beers: {beers.count('Aldaris')}")

# existance of Aldaris beer in the list
if "Aldaris" in beers: # so in will be True or False
    print("Aldaris is in the list")

# let's remove all Aldaris beers from the list
# we can use remove() method - it will remove only the first occurrence
# we can check if Aldaris is present in the list before removing
while "Aldaris" in beers:
    beers.remove("Aldaris") # IN PLACE method - modifies the list

print(f"Beers: {beers}")

# one note about in check for lists
# in check for lists is slow for large lists - it has to go through all items (alternative use dict or set)

# show our beer list
print(f"Beers: {beers}")
# now let's reverse it
# again we have two approaches - OUT OF PLACE and IN PLACE
# TWO OUT OF PLACE approaches
reversed_beers = list(reversed(beers)) # this will create a new list, reversed does not return a list
print(f"Reversed beers: {reversed_beers}")
also_reversed_beers = beers[::-1] # this will create a new list, this is slicing approach
print(f"Also reversed beers: {also_reversed_beers}")
# note we use reversed if we need to go through the list in reverse order - more efficient than slicing
print(f"Original beers: {beers}")
# IN PLACE approach - modifies the original list
beers.reverse() # IN PLACE - modifies the original list to the reversed order
print(f"Reversed original beers: {beers}")
# let's go back
beers.reverse() # IN PLACE - modifies the original list to the original order
print(f"OG Beers: {beers}")

# let's remove one occurrence of Tērvetes
beers.remove("Tērvetes") # IN PLACE method - modifies the list
print(f"Beers: {beers}")

# we can also find index of an item in the list
# let's find index of Labietis
index = beers.index("Labietis") # it will return the index of the first occurrence
print(f"Index of Labietis: {index}")
# for lists we do not have find() method - we have to use index() method
# this means it will throw an error if the item is not in the list
# we could use in check before calling index() method
needle = "Zoltners"
if needle in beers:
    index = beers.index(needle)
    print(f"Index of {needle}: {index}")
else:
    print(f"{needle} is not in the list")

# alternative approach is to use try-except block
try:
    index = beers.index(needle) # so index will throw an error if the item is not in the list
    print(f"Index of {needle}: {index}")
except ValueError:
    print(f"{needle} is not in the list")

# again we can use . to access methods of an object
# visual studio code and other IDEs will show you all available methods after pressing .

# last but not least we can clear the list
beers.clear() # IN PLACE method - modifies the list and removes all items
print(f"Beers: {beers}")

# we can add more items now again with append or extend methods
beers.append("Labietis")
beers.extend(["Piebalgas", "Valmiermuižas"])
print(f"Beers: {beers}")

# Full Documentations on List methods
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# real python - lists
# https://realpython.com/python-lists-tuples/


