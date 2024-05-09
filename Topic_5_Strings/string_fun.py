# let's explore strings in Python

# Strings are sequences of characters
# Strings are immutable
# Strings can be indexed and sliced

# Strings can be created using single quotes
food = 'pizza'
print(food)

# Strings can be created using double quotes
drink = "coffee"
print(f"I like to drink {drink}")

# in Python there is no difference between single and double quotes

# Why is it useful to have both single and double quotes?
# If you want to use a quote inside a string

quote = "He said, 'I am hungry'" # note the use of double quotes
print(quote)

# otherwise I would have to use escape characters
quote = 'He said, \'I am hungry\''
print(quote)

# list escape characters
# \n - newline
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote
# there are a few others

# let's make a string with some newlines
s = "Hello\nWorld"
print(s)

# for longer strings, we can use triple quotes
# this is useful for docstrings and other multi-line strings
long_string = """This is a long string
that spans multiple lines
    and uses triple quotes      
    Can use single or double quotes inside this string
for example 'single quotes' or "double quotes"
only thing we can not use is triple quotes :)
"""

# we can use f-strings in Python 3.6 and later
# f-strings allow us to embed expressions inside strings
name = "Valdis"
age = 50
f_string = f"My name is {name} and I am {age} years old"
print(f_string)

# I can use expressions inside f-strings
# for example I can do math
# I can call functions
# I can access variables

PI = 3.1415926
r = 10

area = PI * r ** 2
area_string = f"The area of a circle with radius {r} is {area}"
print(area_string)
# i can format the numeric output to specific number of decimal places
area_string = f"The area of a circle with radius {r} is {area:.2f}" # note the :.2f
print(area_string)
# the actual area is not rounded, only the output is rounded - unlike round function
# we can add padding to our output
area_string = f"The area of a circle with radius {r:05} is {area:.2f}" # note the :05
print(area_string)

# Documentation on f-strings
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings