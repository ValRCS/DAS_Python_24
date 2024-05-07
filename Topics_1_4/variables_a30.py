# so variables are fundamental building block in most prog languages
# in Python variables are declared and used whenever we use =
# data types are dynamically assigned on whatever we are assigning
# name = "Valdis" # maybe there will be a different name
# variables should start with a letter upper or lower
# variables can have numbers in them and also underscore _
# good variable names should be descriptive
# do not use a,b,c unless it is for very short code
# x,y is fine to use for 2d coordinates
# i is fine for loops
# t - temp again for short code snippets
# ideal variables are one or two words long
# for multiple word variables Python style guide recommends _ as separate
# other languages use camelCase for one
# you could use camelCase but then stick to it
# Pythonists recommend snake case
# https://peps.python.org/pep-0008/#function-and-variable-names
# vERyBadVariable name but legal...
this_is_very_long_variable_that_i_am_not_using = 0 # too long in real life
PRECISION = 2 # used for results could have called this RESULT_PRECISION
# UPPERCASE generally indicated constants by convention
# technically we can change them

name = input("What is your name friend?")
# input ALWAYS returns string after user presses enter in console
# print(name)
# print("Hello",name)
# print("Hello "+name)
# # f-strings formatted strings
# print(f"Hello {name}") # so f in front of string means formatted strings
# we can put variables and expression inside f-string {}
print(f"Why that's a nice name {name}!")
print(f"Wish there were more people named {name} in the world 😉")
# new line is automatic for print
# if I do not want new line I use end="" inside print call
print(f"What is your favorite food {name}?", end="") 
food = input() # empty input will not show any text
print(f"Wow I love {food} as well, {name}!")
quantity = input(f"How many kg of {food} do you want to buy {name}?")
price = input(f"How much are {food} in your neck of woods {name}?")
# careful here..
# first we should cast our relevant strings to numbers(floats or integers)
# let's assume only whole numbers for quantity
# let's assume any number (float) for price
# today we trust user to give good input
quantity = int(quantity) # Python will attempt to change data type to int
price = float(price) # again Python will try to cast price to float
# in real we can not trust input - so error is possible here
# we will handle errors in another lecture
total = quantity * price
print(f"So it would cost {total} € for {quantity} kg of {food}")
# it might be a good idea to round the price to some digits
# for example 2 digits after comma
# in general we want to avoid magic numbers
# 2 could have multiple uses (different formulas etc)
# much better to have them as variables or constants
total_rounded = round(total, PRECISION) # i could have overwritten total instead if I wanted
print(f"Actually it would cost {total_rounded} € for {quantity} kg of {food}")

