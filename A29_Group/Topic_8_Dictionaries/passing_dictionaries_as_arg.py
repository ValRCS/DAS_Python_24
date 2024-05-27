# just like lists, dictionaries can be passed as arguments to functions
# we have to be careful if we want to modify the dictionary
# when dictionary is passed to a function, it is passed by reference - so aliasing can occur
# so if we adjust the function parameter, we will also adjust the original dictionary

# let's see an example
def adjust_age(person_dict):
    person_dict["age"] += 5 # original will ALSO be changed
    # we could return the dictionary, but it is not necessary
    return person_dict # not really needed in this case

person = {"name": "Janīna", "age": 30}
print(person)
dict_alias = adjust_age(person)
print(person)
print(dict_alias)

# if we do not want to modify the original dictionary, we can pass a copy
# we can use .copy() method or dictionary unpacking
def get_older_dict(person_dict):
    person_dict = person_dict.copy() # we have a copy of the dictionary so original is safe
    person_dict["age"] += 5
    return person_dict

person = {"name": "Līga", "age": 25}
print(person)
dict_copy = get_older_dict(person)
print(person)
print(dict_copy)

# one last warning is for dictionaries do not adjust size when looping
# this means no deletion no addition of keys when looping
# instead we can create a new dictionary and add keys there

# example
food_prices = {"apple":1.64, "banana":0.99, "cherry":2.99, "date":1.99, "elderberry":3.49}
# so if i want to remove all fruits that cost less than 2
# i cannot do it directly in the loop
# instead i could create a new dictionary
expensive_fruits = {}
for fruit, price in food_prices.items():
    if price >= 2:
        expensive_fruits[fruit] = price

# original is not affected
# I could have done this with dictionary comprehension
also_expensive_fruits = {fruit: price for fruit, price in food_prices.items() if price >= 2}

# original
print(food_prices)
# let's print both
print(expensive_fruits)
print(also_expensive_fruits)