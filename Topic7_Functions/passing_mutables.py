# we can creat functions that will modify mutable objects
# primitive types are immutable
# primitive types are int, float, bool, str, tuple
# all other types are mutable

# let's say I want to write a function that will add a new element to a list
# but it will only do so if the element is not already in the list

def add_unique_element_to_list(element, my_list):
    # first let's check if it is a list
    # usually we do not do this for Python functions
    # but for crucial functions it is a good idea
    # it is a question whether we can continue working on bad data
    if not isinstance(my_list, list):
        print("Second parameter should be a list")
        return # None is returned by default
    if element not in my_list:
        my_list.append(element)
    else:
        print(f"{element} is already in the list")
    # I could return my_list but it is not necessary


foods = ["apple", "banana", "carrot"] # foods live globally
add_unique_element_to_list("apple", foods)
add_unique_element_to_list("date", foods)
print(foods)

# now let's make a function that returns a new list with unique elements
# in reality we could have used set but let's assume we do not know about it
def unique_list(input_list):
    # first let's check if it is a list
    if not isinstance(input_list, list):
        print("Parameter should be a list")
        return # None is returned by default
    new_list = [] 
    for element in input_list:
        if element not in new_list: # this could get slow on large lists
            new_list.append(element)
    return new_list # original is not affected!

# let's test it
foods = ["apple", "banana", "carrot", "apple", "banana", "date"]
unique_foods = unique_list(foods)
print("Uniques", unique_foods)