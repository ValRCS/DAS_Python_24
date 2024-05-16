# Until now we have been writing scripts - essentially everything we have written has been a script.
# that is a series of commands that are executed in order - with some control structures to change the order of execution.
# that is all fine but for larger programs it is useful to be able to define functions.

# let's say I have some instruction on eating a sandwich
# I could write a script like this:
# print("Take two slices of bread")
# print("Put some cheese on one slice")
# print("Put some ham on the other slice")
# print("Put the slices together")

# problem is when I want to do this multiple times
# then I have to COPY PASTE the instructions

# better would be to combine the instructions into a function
# function is a block of code that has a name(for now) and can be executed by calling that name

# Defining a function
def make_sandwich(): # note the () - this is where we would put parameters if we had any
    print("Take two slices of bread")
    print("Put some cheese on one slice")
    print("Put some butter on other slice")
    print("Put some ham on the other slice")
    print("Put the slices together")

# now that I have defined this function I can call it by using its name
# make_sandwich()
# # I can call it multiple times
# for _ in range(5): # in Python if I do not need the variable I can use _ instead of a name
#     make_sandwich()

# we can pass parameters to functions
# let's make a function to make a sandwich with a given filling
def make_sandwich_with(filling):
    print("Take two slices of bread")
    print(f"Put some {filling} on one slice")
    print("Put some butter on other slice")
    print("Put some ham on the other slice")
    print("Put the slices together")

# make_sandwich_with("cheese")
make_sandwich_with("tomato")

# let's make a function that makes a sandwitch it will take two parameters
# type of bread and also a list of fillings
def make_sandwich_with_bread_and_fillings(bread, fillings):
    print(f"Take two slices of {bread}")
    try:
        for filling in fillings:
            print(f"Put some {filling} on one slice")
    except TypeError:
        print("Fillings should be iterable - preferably a list")
    print("Put the slices together")

make_sandwich_with_bread_and_fillings("rye", ["cheese", "ham", "tomato"])
# i can use rice cake as bread and healthy fillings
make_sandwich_with_bread_and_fillings("rice cake", ["avocado", "tomato", "lettuce"])

# now note that Python does not check parameter types
# so i could pass string as second parameter and it would work...sort of
make_sandwich_with_bread_and_fillings("rye", "cheese")
# this is because Python treats strings as a list of characters
# if I pass a number as a second parameter it will not work
make_sandwich_with_bread_and_fillings("rye", 5)

# let's define a simple add function
def print_add(a, b):
    print(f"{a} + {b} = {a + b}")

print_add(5, 6)
# above function prints but we have no way of saving the result
# we can return the result

def add(a, b):
    return a + b # means I can pass the result of this function to another function or save it in a variable

result = add(5, 6) # now I can save the result
print(f"5 + 6 = {result}")

# lets multiply two numbers
def multiply(a, b):
    return a * b

result = multiply(5, 6) # of course I could have used a different variable name
print(f"5 * 6 = {result}")

# now I can combine both multiple and add functions
result = add(multiply(5, 8), add(3,10)) # so we can nest function calls
print(f"(5 * 8) + (3 + 10) = {result}")

result = print_add(5,10) # this will not work as print_add does not return anything
print(f"5 + 10 = {result}") # this will show None as result
# so if we do not return anything from a function it will return None

# famously print function does not return anything
# print is a classical side effect function - it does something but does not return anything

# there is this idea of pure functions - functions that do not have side effects
# pure functions return a value and do not change anything outside of the function

# so let's make a function that gets integer input from user
def get_integer_input(prompt):
    while True:
        try:
            # return int(input(prompt)) # most concise
            # same with variables - not needed but not wrong
            user_input = input(prompt)
            number = int(user_input)
            return number # upon return user_input and number are destroyed
            # the error if there is one would occur on int conversion not return
        except ValueError:
            print("That was not an integer")

x = get_integer_input("Give me x coordinate: ")
y = get_integer_input("Give me y coordinate: ")
print(f"Coordinates are ({x}, {y})")
# multiply
result = multiply(x, y)
print(f"{x} * {y} = {result}")

# i could call my input functions inside the multiply function
result = multiply(get_integer_input("Give me x: "), get_integer_input("Give me y: "))
# however the code is less readable
print(f"Result is {result}")

