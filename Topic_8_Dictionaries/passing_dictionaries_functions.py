# passing dictionaries to functions
# when passing dictionaries to functions you need to check 
# what kind of methods you will be applying inside the function
# if those will be changing the dictionary, then you might want to pass a copy
# if the methods inside the function will not be changing the dictionary, then you can pass the dictionary itself

food_prices = {'apple': 0.99, 
               'banana': 0.59, 
               'orange': 0.79,
               'kiwi': 1.99,
                'blueberry': 4.99,
                'potatoes': 0.49
                }

# let's see an example
def print_prices(prices):
    '''This function will print all prices in the dictionary'''
    for food, price in prices.items():
        print(f"Price of {food} is {price}")

print_prices(food_prices)

# now how about filter out some prices
def get_cheap_foods(prices, threshold=1.0):
    '''This function will return a dictionary with foods under 1 Euro'''
    cheap_foods = {food: price for food, price in prices.items() if price < threshold}
    # dictionary comprehension is always creating a new dictionary so safe to return
    return cheap_foods

cheapies = get_cheap_foods(food_prices, 0.75)
print(cheapies)

# how could we do this without dictionary   comprehension
def get_cheap_foods_no_comprehension(prices, threshold=1.0):
    '''This function will return a dictionary with foods under 1 Euro'''
    cheap_foods = {} # new dictionary so again original dictionary is not changed
    for food, price in prices.items():
        if price < threshold:
            cheap_foods[food] = price
    return cheap_foods

cheapies = get_cheap_foods_no_comprehension(food_prices, 0.75)
print(cheapies)

# there is another approach where we could be deleting the expensive items from the original dictionary
# here we have to be careful as we are changing the original dictionary

def get_cheap_foods_delete_expensive_in_place(prices, threshold=1.0):
    '''This function will return a dictionary with foods under 1 Euro
    IN PLACE - so it will change the original dictionary'''
    for food, price in list(prices.items()): # we are making a list from the dictionary items
        if price >= threshold:
            del prices[food] # so we are deleting from the original dictionary
    return prices # so we are returning the original dictionary but changed, in fact we could returning nothing and still have the same effect

cheapies = get_cheap_foods_delete_expensive_in_place(food_prices, 1.0)
print(cheapies)
print(f"IS cheapies same as food_prices? {cheapies is food_prices}") # so we are returning the same dictionary but changed

# alternative would be to make a copy of the dictionary and then delete the expensive items
# this way we are not changing the original dictionary
food_prices = {'apple': 0.99, 
               'banana': 0.59, 
               'orange': 0.79,
               'kiwi': 1.99,
                'blueberry': 4.99,
                'potatoes': 0.49
                }

def get_cheap_foods_delete_expensive_copy(prices, threshold=1.0):
    '''This function will return a dictionary with foods under 1 Euro
    OUT OF PLACE - keeps the original dictionary unchanged'''
    prices = prices.copy() # so we are making a copy of the original dictionary
    # so now prices is a new dictionary and we can delete from it
    for food, price in list(prices.items()): # we are making a list from the dictionary items
        if price >= threshold:
            del prices[food] # so we are deleting from the original dictionary
    return prices # so we are returning the new dictionary

cheapies = get_cheap_foods_delete_expensive_copy(food_prices, 1.0)
print(cheapies)
print(f"IS cheapies same as food_prices? {cheapies is food_prices}") # so we are returning a new dictionary
print(food_prices) # so original dictionary is unchanged

# again we have two main approaches 
# 1. BUILD UP a new dictionary
# 2.a DELETE from the original dictionary or 2b. DELETE from a copy of the original dictionary