# just like lists have list comprehension, dictionaries have dictionary comprehension
# idea is to provide a way to create dictionaries in a more concise way
# here is an example
# let's say we have a list of foods and we want to create a dictionary of food prices
foods = ['apple', 'banana', 'orange']
# prices = [0.99, 0.59, 0.79]
# we could have used zip function to combine the two lists
# food_prices = dict(zip(foods, prices)) # this is great but does not allow for any transformation
# let's say i want length of strings as values
# without dictionary comprehension I would have to do this
food_lengths = {} # typical start with nothing - empty dictionary
for food in foods:
    food_lengths[food] = len(food) # so now I have apple:5, banana:6, orange:6
print(food_lengths)
# instead we could use dictionary comprehension
also_food_lengths = {food: len(food) for food in foods} # so much more concise
print(also_food_lengths)

# often we need to filter out some values
# again let's have some food prices
food_prices = {'apple': 0.99, 
               'banana': 0.59, 
               'orange': 0.79,
               'kiwi': 1.99,
                'blueberry': 4.99,
                'potatoes': 0.49
                }
# let's say I want a new dictionary only with under 1 Euro price
# without dictionary comprehension I would have to do this
cheap_foods = {}
for food, price in food_prices.items():
    if price < 1:
        cheap_foods[food] = price
print(cheap_foods)
# with dictionary comprehension
also_cheap_foods = {food: price for food, price in food_prices.items() if price < 1}
# note items() method is used to get key-value pairs and we can use if to filter out
print(also_cheap_foods)
# let's double the price for all foods under 1 Euro
kwiki_mart_prices = {food: price*2 for food, price in food_prices.items() if price < 1}
print(kwiki_mart_prices)
# now if I wanted to keep the expensive items and change the cheap ones
kwiki_mart_prices.update({food: price for food, price in food_prices.items() if price >= 1})
print(kwiki_mart_prices)

# instead I could have done this approach with a loop
kwiki_mart_prices = {}
for food, price in food_prices.items():
    if price < 1:
        kwiki_mart_prices[food] = price*2
    else:
        kwiki_mart_prices[food] = price
print(kwiki_mart_prices)

# so dictionary comprehension is not always the best approach, but it is often more concise
