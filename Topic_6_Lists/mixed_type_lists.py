# Python lists lets us store multiple items in a single variable no matter the type
# TIP: try to keep your lists homogeneous, meaning all elements should be of the same type
# TIP: if you have to mix types in a list you can always check the type of each element
mixed_list = [1, 2, 3, 
              "Valdis", "Programmer", "Ventspils", 
              3.14, 2.71, 0.0, 
              -1, -2, -3, 
              None, False, True,
              [50, 2, 3]]
print(mixed_list)

# we can loop through the list and check the type of each element
for item in mixed_list:
    print(item, type(item))

# so we can either use try except approach or check the type of each element

# so let's say we want to sum all the numbers in the list
# we could use a for loop
sum_numbers = 0
for item in mixed_list:
    if type(item) in [int, float]: # so we check if the type is int or float
        sum_numbers += item
    # if nested list we could loop through that as well
    elif type(item) == list:
        for nested_item in item:# we have guaranteed that item is a list
            if type(nested_item) in [int, float]:
                sum_numbers += nested_item
print(round(sum_numbers,4))

print(type(5))
# is 5 int
print(isinstance(5, int))
# or alternative is in
print(type(5) in [int, float, str])