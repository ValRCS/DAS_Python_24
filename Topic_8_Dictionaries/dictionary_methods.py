# dictionaries have their own methods
# we already saw items() method for iterating over key-value pairs
# we also say keys() and values() methods which return keys and values respectively as list like objects 

# let's see some examples
# let's say we have a dictionary of food prices
food_prices = {'apple': 0.99, 'banana': 0.59, 'orange': 0.79}
# we want to get price of some food which we are not sure is in the dictionary
# one approach would be to check first if the key exists
# needle = 'banana'
needle = 'kiwi'
if needle in food_prices:
    print(f"Price of {needle} is {food_prices[needle]}")
else:
    print(f"Price of {needle} is not available, no such key in the dictionary!")

# above is very common operation, so there is a method for that
# instead we can use get method
# get method takes key as first argument and default value as second
# if key exists, it returns the value, if not, it returns the default value
price = food_prices.get('banana')
print(f"Price of banana is {price}")
price = food_prices.get('kiwi') # so if key does not exist, it will return None
print(f"Price of kiwi is {price}")
# instead I could decide I want default price to be 0.01
price = food_prices.get('kiwi', 0.01)
print(f"Price of kiwi is {price}") # so now it will return 0.01 if key does not exist

# reminder no need for get if we are looking for a key that we are sure exists
# for example when looping over keys we can be sure that key exists so no need for get

# let's see some more methods
# there is a setdefault method
# idea is to set a default value for a key if it does not exist otherwise return the value but do not change
# let's say we want to set price of kiwi to 1.99 if it does not exist
price = food_prices.setdefault('kiwi', 1.99) # price part is optional if we do not care for the value
print(f"Price of kiwi is {price}")
# now let's try to increase the price of kiwi to 3.50 using setdefault
price = food_prices.setdefault('kiwi', 3.50) # so this time it will not change the value
print(f"Price of kiwi is {price}")
print(food_prices) # so price of kiwi is still 1.99
# of course I could change the price to 3.50 using direct assignment
food_prices['kiwi'] = 3.50
print(food_prices) # so now price of kiwi is 3.50
# how about increasing price by 0.25
food_prices['kiwi'] += 0.25 # same as food_prices['kiwi'] = food_prices['kiwi'] + 0.25
# of course above assume that key kiwi exists, so we should check that first
print(food_prices) # so now price of kiwi is 3.75

# just like with lists = is alias, so it is with dictionaries
food_prices_alias = food_prices # just a reference to the same dictionary
# however I can make a copy of dictionary using copy method
food_prices_copy = food_prices.copy() # so now I have two different dictionaries
# so if I change one, the other will not be affected

# let's try changing some price in food_prices_alias
# let's add blueberry
food_prices_alias['blueberry'] = 4.99 # will affect both food_prices and food_prices_alias but not food_prices_copy
print(food_prices)
print(food_prices_alias)
print(food_prices_copy)

# let's see how to remove a key-value pair
# let's say we want to remove blueberry
del food_prices['blueberry'] # is one approach
print(food_prices)
# another approach is to use pop method
# pop method takes key as argument and returns the value
price = food_prices.pop('banana') # price =  is optional if we do not care for the value
print(f"Price of banana was {price}")
print(food_prices)
# if key does not exist, pop will raise an error
try:
    price = food_prices.pop('banana')
except KeyError as e:
    print(f"Error: {e}")

# if we do not want to raise an error, we can use pop with default value
price = food_prices.pop('banana', None) # so now price will be None or any other value if key does not exist
print(f"Price of banana could have been {price}")
# note that del also would raise an error if key does not exist
try:
    del food_prices['banana']
except KeyError as e:
    print(f"Error: {e}")

# let's see how to remove all key-value pairs
food_prices.clear() # IN PLACE so nothing left in food_prices
print(food_prices)

try:
    food_prices.popitem() # will remove a random key-value pair, but here it is empty so will raise an error
except KeyError as e:
    print(f"Error: {e}")

# let's see how to update a dictionary with another dictionary
# let's say we have another dictionary with some prices
food_prices = {'apple': 0.99, 'banana': 0.59, 'orange': 0.79}
# and we have another dictionary with some more prices
more_food_prices = {'banana':1.27,'kiwi': 1.99, 'blueberry': 4.99}
# so when I apply update method, it will update the prices of existing keys and add new keys
food_prices.update(more_food_prices) # IN place for food_prices
print(food_prices) # so now banana price is 1.27, kiwi is 1.99 and blueberry is 4.99

new_dict = food_prices.fromkeys(['apple', 'banana', 'kiwi','potatoes'], 0.99) # so this will create a new dictionary with keys from the list and default value
print(new_dict) # so all keys have value 0.99
# note that potates is not in food_prices  but we got the key anyway
# this means that we do not need a specific dictionary to use fromkeys method
# instead we could use dict class
new_dict = dict.fromkeys(['apple', 'banana', 'kiwi','potatoes'], 0.99)
print(new_dict) # so all keys have value 0.99 handy for setting default values


