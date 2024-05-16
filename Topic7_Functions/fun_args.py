# so print function has this ability to take multiple arguments and keyword arguments
# for example
print("Valdis", "Līga", "Rūta", "Liene", sep="|X|", end="!\n")

# we can do the same in our functions
# let's make a function that eats a meal that can have multiple ingredients
def eat_meal(*ingredients, drink="water"):
    # so ingredients will be a tuple (fixed list) of all arguments passed to the function
    # we can loop over all arguments
    print("Eating a meal with:")
    for ingredient in ingredients:
        print(ingredient)
    print(f"Drinking {drink}")

eat_meal("potatoes", "carrots", "meat", "salad", "bread")
# notice that without using named parameter drink we will get the default value
eat_meal("potatoes", "carrots", "meat", "salad", "bread", "wine")
# instead we can use named parameter drink
eat_meal("potatoes", "carrots", "meat", "salad", "bread", drink="wine") # most likely what we want

# we can also have required parameters before *args
# for example let's say we want to have a meal with a name
def eat_named_meal(meal_name, *ingredients, drink="water"):
    print(f"Eating {meal_name} with:")
    for ingredient in ingredients: # these are all optional
        print(ingredient)
    print(f"Drinking {drink}") # this will have a default value of water unless we specify otherwise

eat_named_meal("Succulent chinese meal", "rice", "noodles", "duck", "soy sauce", drink="beer")

# or course we could have also made a function that receives a list of ingredients not a variable number of arguments
# for example
def eat_list_meal(meal_name, ingredients, drink="water"): #  here ingredients should be iterable!
    print(f"Eating {meal_name} with:")
    for ingredient in ingredients: # these are all optional
        print(ingredient)
    print(f"Drinking {drink}") # this will have a default value of water unless we specify otherwise

eat_list_meal("Succulent chinese meal", ["rice", "noodles", "duck", "soy sauce"], drink="beer") # note the list brackets

# one thing you should not do and that is supply a default mutable object as a default value such as list or dictionary
# because then all calls to that function will share the same mutable object
# instead you should use a None default value and then check if the parameter is None and then assign a new list or dictionary
# for example
def add_to_list(new_element, my_list=None): # so again do not put my_list=[] as default value !!!!
    if my_list is None:
        my_list = []
    my_list.append(new_element)
    return my_list