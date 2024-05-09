# let's explore strings in Python

# Strings are sequences of characters
# Strings are immutable
# Strings can be indexed and sliced

# Strings can be created using single quotes
food = 'kartupelis'
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

# i can use f-strings with triple quotes
# this is useful for multi-line strings
# this is useful for docstrings

long_string = f"""This is a long string
that spans multiple lines
    and uses triple quotes      
    Can use single or double quotes inside this string
for example 'single quotes' or "double quotes"
we can use variables and expressions inside f-strings
for example PI is {PI} and r is {r}
the area of a circle with radius {r} is {area:.2f}
"""
print(long_string)

# now how about getting length of a string
# we can use len function
food_length = len(food)
print(f"Length of {food} is {food_length}")

# now we can start accessing our string letter by letter
# we can use indexing
# in Python we use 0-based indexing using []

# first letter
first_letter = food[0] # note the 0 index
print(f"First letter of {food} is {first_letter}")
second_letter = food[1]
print(f"Second letter of {food} is {second_letter}")

# how about last one?
# we could use len function that we just learned
# or we could use -1 index
# first the last letter with length
index_last = len(food) - 1
last_letter = food[index_last]
print(f"Last letter of {food} is {last_letter} it is at index {index_last}")

# we can use negative indexing
# Python offers two indexing methods
# we can go backwards using negative indexes
# last letter
last_letter = food[-1] # same as food[len(food) - 1]
print(f"Last letter of {food} is {last_letter}")

# also see https://developers.google.com/edu/python/strings for more string exercises

# so second to last letter?
second_last_letter = food[-2]
print(f"Second to last letter of {food} is {second_last_letter}")
print(f"Its negative index is -2")

# How about what happens if we try out of bounds index?
try:
    out_of_bounds = food[10] # remember we start from 0 so 10 is out of bounds(it would be 11th letter)
except IndexError as e:
    print(f"IndexError {e}")

# how about getting more than one letter?
# in Python we can use slicing

# let's get first 3 letters
# slicing full syntax is [start:stop:step]
# we can omit start, stop or step
# if we omit start, it is 0
# if we omit stop, it is end of the string
# if we omit step, it is 1

# so let's get first 3 letters
first_three = food[:3] # same as food[0:3]
# so we start from 0 and go up to 3 but not including 3,because index 3 is actually 4th letter
print(f"First three letters of {food} are {first_three}")

# we can slice from the end
# let's get last 3 letters
last_three = food[-3:] # same as food[-3:len(food)]
# we start from -3 and go to the end
print(f"Last three letters of {food} are {last_three}")

# how about middle
middle = food[3:6] # we start from 3(4th letter) and go up to 6(7th letter) but not including 6
print(f"Middle letters of {food} are {middle}")
# now let's get all letters except first 3 and last 3
middle = food[3:-3] # we start from 3(4th letter) and go up to -3 but not including -3 (last 3 letters)
print(f"Middle letters of {food} are {middle}")

# we can use step
# first let's get our english alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz" # we could have used import string; alphabet = string.ascii_lowercase
# let's get every second letter
every_second = alphabet[::2] # we start from 0 and go to the end with step 2
print(f"Every second letter of the alphabet is {every_second}")
# we could start with second letter
every_second = alphabet[1::2] # we start from 1 and go to the end with step 2
print(f"Every second letter of the alphabet starting from b is {every_second}")
# how about starting from 4th and ending before last 3 and step 3
every_third = alphabet[3:-3:3] # we start from 3 and go up to -3 but not including -3 with step 3
print(f"Every third letter of the alphabet starting from d and ending before x is {every_third}")

# we can reverse a string
reverse_food = food[::-1] # we start from the end and go to the beginning with step -1
print(f"Reverse of {food} is {reverse_food}")
# we could have used other negative step values
reverse_food = food[::-2] # we start from the end and go to the beginning with step -2
print(f"Every second letter of the reverse of {food} is {reverse_food}")

# note that strings are immutable
# so if we want to change a string we have to create a new one
# we can concatenate strings
# we can use + operator
# we can use += operator to update the string
# we can use join method
# we can use f-strings

# existance check in strings
# we can use in keyword
# we can use not in keyword

# let's check if our food has letter a
if 'a' in food:
    print(f"Waiter {food} has letter a!")
else:
    print(f"Waiter {food} does not have letter a!")

# more generically we can say needle in haystack
needle = "art"
if needle in food:
    print(f"Waiter {food} has {needle}!")
else:
    print(f"Waiter {food} does not have {needle}!")

# we can also use find method
# find returns the index of the first occurance of the substring
# if substring is not found, find returns -1
# we can also use rfind method to find the last occurance of the substring (from right)

# let's find the index of letter a
index_a = food.find('a')
print(f"Index of letter a in {food} is {index_a}")
needle = "art"
index_art = food.find(needle)
print(f"Index of {needle} in {food} is {index_art}")
bad_needle = "xyz"
index_xyz = food.find(bad_needle)
print(f"Index of {bad_needle} in {food} is {index_xyz}")
# we could use it in if statement
if food.find(bad_needle) == -1:
    print(f"Waiter {food} has {bad_needle}!")

# there is also index method
# index method is similar to find method
# index method raises ValueError if substring is not found
# example with index method
try:
    index_xyz = food.index(bad_needle)
    # so if we get here, we know that bad_needle was found
    print(f"Index of {bad_needle} in {food} is {index_xyz}")
except ValueError as e:
    print(f"ValueError {e}")
    # good for cases when we can handle the error somehow - change the needle or ignore the error

# we can count the number of occurances of a substring
# we can use count method
# count method returns the number of occurances of the substring

# let's count the number of a's in food
haystack = "ABBBBA"
needle = "B"
count = haystack.count(needle)
print(f"Number of {needle}'s in {haystack} is {count}")
# note that count is non-overlapping - careful when counting more than one letter
needle = "BB"
count = haystack.count(needle)
print(f"Number of overlapping {needle}'s in {haystack} is {count}") # 2 NOT 3 !

# let's count overlapping strings using for loop
haystack = "ABBBBA"
needle = "BB"
count = 0
for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i+len(needle)] == needle: # we compare the substring with needle
        print(f"Found {needle} at index {i}")
        count += 1
print(f"Number of overlapping {needle}'s in {haystack} is {count}")

# usually when we loop through a string we use for loop without range
# we can loop through a string letter by letter
for letter in food:
    print(letter)

# if we need indexes we can use enumerate
for index, letter in enumerate(food):
    print(f"Index {index} has letter {letter} really {food[index]}")

# avoid for in range(len()) when possible - not considered pythonic

# now let's look at some more string methods
# we can use lower method to convert a string to lower case
city = "Rīga"
city_lower = city.lower()
print(f"{city} in lower case is {city_lower}")
# same for upper
city_upper = city.upper()
print(f"{city} in upper case is {city_upper}")
# title will capitalize the first letter of each word
sentence = "Nice sunny day"
sentence_title = sentence.title()
print(f"{sentence} in title case is {sentence_title}")
# capitalize will capitalize the first letter of the string
sentence = "nice sunny day"
sentence_capitalize = sentence.capitalize()
print(f"{sentence} in capitalize case is {sentence_capitalize}")
# rarer is swapcase which will swap the case of each letter
sentence = "Nice Sunny Day"
sentence_swapcase = sentence.swapcase()
print(f"{sentence} in swapcase case is {sentence_swapcase}")

# note in Visual Studio Code if we have a string we can use . to see all available methods
# we can also use help(str) to see all available methods
# full docs on string methods https://docs.python.org/3/library/stdtypes.html#string-methods

# useful method is replace
# replace will replace all occurances of the substring with another substring
# replace returns a new string - original string is not changed
sentence = "I like to drink coffee"
new_sentence = sentence.replace("coffee", "tea")
print(f"Original sentence is {sentence}")
print(f"New sentence is {new_sentence}")
# i could overwrite the original string
sentence = sentence.replace("coffee", "tea")
print(f"Overwritten sentence is {sentence}")

# let's create a new string by iterating over the old one
# let's replace all a's with x's
# we could have done it with replace method but let's do it manually
food = "kartupelis mans mīļākais ēdiens"	# kartupelis mans mīļākais ēdiens
new_food = "" # typical idea with start with empty string # often called buffer
# let's also count
count = 0
for letter in food:
    # the idea is that I keep adding letters to new_food
    # but if I see letter a, I add x instead
    if letter == 'a':
        new_food += 'x'  # += is the same as new_food = new_food + 'x'
        count += 1
    else:
        new_food += letter  # I add original letter

print(f"Original food was {food}")
print(f"New food is {new_food}")
print(f"Number of a's replaced with x's is {count}")

# now let's talk at cleaning methods
# strip method will remove leading and trailing whitespace
dirty_city = "  Rīga  "
clean_city = dirty_city.strip()
print(f"Dirty city is '{dirty_city}'")
print(f"Clean city is '{clean_city}'")
# there is also lstrip and rstrip
# lstrip will remove leading whitespace
# rstrip will remove trailing whitespace
dirty_city = "  Rīga  "
clean_city = dirty_city.lstrip()
print(f"Dirty city is '{dirty_city}'")
print(f"Clean city is '{clean_city}'")
dirty_city = "  Rīga  "
clean_city = dirty_city.rstrip()
print(f"Dirty city is '{dirty_city}'")
print(f"Clean city is '{clean_city}'")

# we can supply specific characters to strip
# let's strip all a's from the beginning and end
dirty_city = "aaaRīgagaaaa"
clean_city = dirty_city.strip('a')
print(f"Dirty city is '{dirty_city}'")
print(f"Clean city is '{clean_city}'") # note that only leading and trailing a's are removed
# we can supply multiple characters
dirty_city = "aaaRīgagaaaa   g aag"
clean_city = dirty_city.strip('ag xyz') # could supply multiple characters to strip
print(f"Dirty city is '{dirty_city}'")
print(f"Clean city after stripping (a and g and whitespace) is '{clean_city}'") 

# then we have startswith and endswith methods
# startswith will check if the string starts with a substring
# endswith will check if the string ends with a substring
# both return True or False
city = "Rīga"
if city.startswith("Rī"):
    print(f"{city} starts with Rī")
if city.endswith("ga"):
    print(f"{city} ends with ga")
