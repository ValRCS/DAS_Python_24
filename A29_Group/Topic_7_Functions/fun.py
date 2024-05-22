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
def round_numbers(numbers, precision    = 0): # precision is a default parameter
    # without list comprehension
    rounded_numbers = [] # so i create an empty list
    for number in numbers:
        rounded_numbers.append(round(number, precision))
    return rounded_numbers # this list will be returned for use by the caller
    # return [round(number) for number in numbers] # list comprehension versions

numbers = [3.14159, 2.71828, 1.61803] # pi, e, golden ratio(phi)
my_rounded_numbers = round_numbers(numbers, 2) # i could have used any name for the variable
print(my_rounded_numbers)