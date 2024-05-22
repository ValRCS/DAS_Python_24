# Until now we have been writing code in the main body of the program.
# Basically that is a script. But we can also write code using our own functions.
# we have already used some of the built-in functions like input(), print(), len(), etc.
# Today we will learn to write our own functions.
# functions are one of the main ways of hiding complexity in programming.

# let's say I want to eat a sandwich. I could go to the store, buy the ingredients, make the sandwich, eat it.
# so using print let's do that.
# print("Go to the store")
# print("Buy the ingredients")
# print("Make the sandwich")
# print("Eat the sandwich")
# this is a simple way of doing things. But what if I want to eat a sandwich again?
# without our own functions we would have to copy and paste the code again. This is not a good practice. So called code smell.
# rule of thumb if you see yourself copy and pasting code, you should probably write a function.

# let's encapsulate the code above in a function.
def eat_sandwich(): # note () and : at the end of the line () is for parameters which we have not used yet.
    print("Go to the store")
    print("Buy the ingredients")
    print("Make the sandwich")
    print("Eat the sandwich")

# now that we have defined this function we can freely use it as many times as we want.
# eat_sandwich()
# eat_sandwich()
# if I wanted to run this code 100 times I would just write eat_sandwich() 100 times.
# or I could write a loop that runs the function 100 times.
# for _ in range(5): # in loops if I do not use the variable I can use _ as a placeholder. This is a convention.
#     eat_sandwich()

# good function does one thing and does it well.

# let's make a function that makes a sandwich.
# for this function it would be nice to have a parameter that tells us what kind of ingredients we need.
def make_sandwich_with(bread): # here we have a parameter called ingredients
    print("Take two slices of " + bread)
    print("Add some ham in between")
    print("Add some cheese")
    print("Add some lettuce")
    print("Add some mayo")
    print("Add some mustard")
    print("Add some pickles")
    print("Add some tomato")
    print("Add some onion")
    print("Now that is some sandwich!")

# now we can make a sandwich with any kind of bread.
# make_sandwich_with("rye")

# we can also make a function that makes a sandwich with any kind of bread and any kind of fillings.
def make_sandwich_with(bread, fillings): # here we have two parameters bread and fillings
    print("Take two slices of " + bread)
    for filling in fillings: # so fillings has to be iterable. We can use a list or even string
        print(f"Add some {filling}" )
    print("Now that is some sandwich!")

my_fillings = ["ham", "cheese", "lettuce", "mayo", "mustard", "pickles", "tomato", "onion"]
my_bread = "rye"
make_sandwich_with(my_bread, my_fillings)
print("All done")

def full_sandwich_production(bread, fillings, number_of_sandwiches):
    # we could check if number_of_sandwiches is an integer and if it is positive
    for _ in range(number_of_sandwiches):
        make_sandwich_with(bread, fillings)
        print("All done")   
    # here _ will be gone as soon as function is done

print("Let's make some sandwiches")
full_sandwich_production(my_bread, my_fillings, 3)
print("Let's eat now...")

# our functions did only printing but did not return any results
# let's say I have a function print_add
def print_add(a, b):
    print(a + b)
    # by defaul functions return None in Python

# if I call this function it will print the result but I cannot use it in any other calculations
print_add(50,20)

result = print_add(50,20)
print(f"Result is {result}") # will be None

# in an ideal world all functions would return something
# in real world sometimes it is okay to return None if the function is just doing some printing or other side effects
# side effects are changes that the function makes outside of its scope
# so printing is a side effect it outputs something to the console
# if a function changes a global variable that is a side effect
# if a function writes to a file that is a side effect
# also if a function sends an email that is a side effect
# read a web page is a side effect

# let's make a function that returns the sum of two numbers
def add(a, b):
    # i could checke some conditions here
    return a + b

result = add(50,20)
print(f"Result is {result}")

# functions without side effects are called pure functions
# those type of functions are easier to test and debug

# ideally functions should be small and do one thing
# so 2 page function is not a good idea most likely you want to break it down into smaller functions

# let's add multiplication to our function
# this let's us return two values
def add_and_multiply(a, b):
    return a + b, a * b  # technically this is a tuple, basically a fixed list - we will learn about them later

addition, multiplication = add_and_multiply(50,20)
print(f"Addition is {addition}")
print(f"Multiplication is {multiplication}")

# for returning more results , one option is a list
# so let's say I want a function that returns rounded values of numbers in a list
def round_numbers(numbers, precision = 0): # precision is a default parameter
    # without list comprehension
    rounded_numbers = [] # so i create an empty list
    for number in numbers:
        rounded_numbers.append(round(number, precision))
    return rounded_numbers # this list will be returned for use by the caller
    # return [round(number) for number in numbers] # list comprehension versions

numbers = [3.14159, 2.71828, 1.61803] # pi, e, golden ratio(phi)
my_rounded_numbers = round_numbers(numbers, 2) # i could have used any name for the variable
print(my_rounded_numbers)
# note that since we have a default parameter we can call the function without the second parameter
really_round_numbers = round_numbers(numbers) # so precision will be 0 here
print(really_round_numbers)

# main idea behind defaults is "sane" defaults - most common use case

# let's say a greeting function
def create_greeting(name="Jāni", greeting = "Labdien"):
    # note no side effects here no printing
    return f"{greeting}, {name}!"

# i can print the result
print(create_greeting("Valdis"))
# we could also save this greeting for later use
my_greeting = create_greeting("Līga", "Sveiki") # so here default is overridden
print(my_greeting)
default_greeting = create_greeting() # so here both defaults are used
# the big assumption here is that Jāni is what we need to use it the most
# in practice usually one of the parameters is changed more often than the other
print(default_greeting)
# it is possible to supply the parameters in any order
print(create_greeting(greeting="Sveiki", name="Maija")) # Note I can use named parameters
# use of named parameters is especially encourage if you have many boolean parameters

# example of function with many Boolean parameters
def create_person(name, 
                  age, 
                  is_student=False, 
                  is_employed=False, 
                  is_married=False):
    # we could do some validation here on sane ages etc
    if age < 0:
        return "Age cannot be negative"
    if age > 122:
        return "Are you sure you are that old?"
    return f"{name} is {age} years old. Student: {is_student}, Employed: {is_employed}, Married: {is_married}"

print(create_person("Valdis", 44, is_student=True, is_employed=True))
# above is much better if I called it without named parameters
print(create_person("Valdis", 44, True, True)) # this is less readable and can lead to errors

# args 
# if we check print function it can take any number of arguments
print("Hello", "World", "and", "Universe")
# we can do the same with our functions
def print_args(*args): # *args is a convention
    print("Let's print all arguments")
    for arg in args: # here we can iterate over all arguments
        print(arg)

print_args("Hello", "World", "and", "Universe")

# alternatively we could use a list
def print_list_args(args): 
    print("Let's print all arguments")
    for arg in args: # here we can iterate over all arguments
        print(arg)

arg_list = ["Alus", "vīns", "degvīns", "ūdens"]
print_list_args(arg_list) # here are I am passing a single list

# we could mix named and unnamed parameters
# here name is REQUIRED, *args is optional
def print_args_with_name(name, *args): # *args is a convention
    print(f"Let's print all arguments for {name}")
    for arg in args: # here we can iterate over all arguments
        print(arg)

print_args_with_name("Valdis", "Hello", "World", "and", "Universe")

# we could even add default values
def print_args_with_name_and_greeting(name, *args, greeting="Hello"): # *args is a convention
    print(f"{greeting} {name}")
    for arg in args: # here we can iterate over all arguments
        print(arg)

print_args_with_name_and_greeting("Valdis", "Pasaule", "and", "Universe")
# in this approach if I want custom greeting I have to use named parameter
print_args_with_name_and_greeting("Valdis", "Pasaule", "and", "Universe", greeting="Sveiki")

# again alternative here would be just to use 3 parameters
# name , words, greeting
# this would be more readable and less error prone
def print_args_with_name_and_greeting(name, words, greeting="Hello"): # *args is a convention
    print(f"{greeting} {name}")
    for word in words: # here we can iterate over all arguments
        print(word)

# one good practice is to create docstrings for your functions
# Python lets us write documention direction in the function definition
# we use triple quotes for this """ or '''
# we finish the docstring with another set of matching triple quotes """ or '''

# let's make a function to buy the ingredients for a sandwich
def buy_ingredients(ingredients):
    """This function buys the ingredients for a sandwich
    It does not return anything"""
    print("Go to the store")
    print("Buy the ingredients")
    for ingredient in ingredients:
        print(f"Buy {ingredient}")

buy_ingredients(["bread", "ham", "cheese"])

# docstrings can be used to generate documentation for your code, generate web pages
# there is a tool called Sphinx that can generate documentation from your docstrings
# URL: https://www.sphinx-doc.org/en/master/index.html
# many Python libraries use Sphinx to generate their documentation

# docstrings work great with type hints

# type hints are a way to tell what type of data a function expects and what it returns
# for example if I have a function that takes two strings and returns their combined length
def combine_lengths(a: str | list, b: str | list) -> int: # so | is used for allowing multiple types
    """This function combines the lengths of two strings or lists or even a mix of both	
    
    Input:

    a - first string\n
    b - second string

    Output:
    int - sum of the lengths"""
    return len(a) + len(b)

# let's use it
result = combine_lengths("Valdis", "Vītols")
print(f"Result is {result}")

# note that len would work on lists as well
# let's try it
result = combine_lengths(["Valdis", "Vītols"], ["Līga", "Maija","Rūta"])
print(f"Result is {result}")

# this could work on say print_list function
def print_list(my_list: list) -> None:
    """This function prints all elements of a list
    
    Input:
    my_list - list of elements to print
    """
    for element in my_list:
        print(element)

print("Let's print a list")
print_list(["Valdis", "Vītols", "Līga", "Maija","Rūta"])
# now if I try printing a single number I will get a warning
# print_list(42)

# we could also print docstring of a function
print(print_list.__doc__) # so __doc__ is a special attribute of functions

# let's make a list of urls to learn more about functions

function_resources = [

# official Python docs
    "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
    "https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions",
    "https://docs.python.org/3/tutorial/controlflow.html#default-argument-values",
    "https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments",
    "https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists",
    "https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists",
    "https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions",
    "https://docs.python.org/3/tutorial/controlflow.html#documentation-strings",
    "https://docs.python.org/3/tutorial/controlflow.html#function-annotations",
    # realpython
    "https://realpython.com/defining-your-own-python-function/",
    "https://realpython.com/python-kwargs-and-args/",
    "https://realpython.com/python-return-statement/",
    # w3schools
    "https://www.w3schools.com/python/python_functions.asp",
    # google's python class
    "https://developers.google.com/edu/python/introduction#user-defined-functions",
]

# let's print out the urls
# but a first a function to do that
def print_resources(resources: list[str]) -> None:
    for resource in resources:
        print(resource)

# print_resources(function_resources)

# passing mutables to functions
# if we pass a list to a function and modify it inside the function it will be modified outside the function as well
# primitives like numbers, strings, booleans are immutable

# let's see an example
def add_to_list(my_list, element):
    my_list.append(element) # so this is IN PLACE method
    return my_list # so same list is return, in fact I could skip this if I did not need the return value

foods = ["bread", "ham", "cheese"]
print(f"Original list: {foods}")
new_foods = add_to_list(foods, "lettuce")
print(f"New list: {new_foods}")
# however if we check the original list it will be modified as well
print(f"Original list: {foods}")
# this means that they are the same list in memory
print(f"Are they the same list? {foods is new_foods}")

# if we want to avoid this we can make a copy of the list
# we can use the copy method
def add_to_list_out_of_place(my_list, element):
    new_list = my_list.copy() # so this is a new list, original outsideis not modified
    new_list.append(element) # so this is IN PLACE method
    return new_list # really new list is returned

really_new_foods = add_to_list_out_of_place(foods, "tomato")
print(f"New list: {really_new_foods}")
print(f"Original list: {foods}")

# again this is for mutable objects like lists, dictionaries, sets and so on
# this does not apply to immutable objects like numbers, strings, booleans

# so takeaway is to be careful if we want to modify some mutable object inside a function

# let's print our resources
print_resources(function_resources)