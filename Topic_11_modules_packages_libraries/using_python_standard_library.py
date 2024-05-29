# Python Standard Library offers a wide range of modules, packages, and libraries to choose from.
# Full Documentation: https://docs.python.org/3/library/

# Let's look at some of these built in libraries
# built in means we just have to use import library_name to use them

# let's look at some text related modules
# string module
# some constants for ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, whitespace
import string
# we can print ascii_lowercase
print(string.ascii_lowercase)
# print digits
print(string.digits)
# print hexdigits
print(string.hexdigits)
# print octdigits
print(string.octdigits)
# print punctuation
print(string.punctuation)

# now let's look re - regular expressions module
# regular expressions are a powerful tool for various text processing tasks
# for those new to regular expressions, it is a mini language for matching text patterns
# you can practice regular expressions at https://regex101.com/ among other places
some_text = "Rīga 2024 DAS Python Kursi Nodarbība 11 Rīga had 800 it was founded in 1201 not in 50000 ..."
# we want to find all years in this text
# years are exactly 4 digits long and have whitespace before and after
# we will import re
import re
# we will use re.findall function
# we will use a regular expression pattern to match 4 digits
# \d is a digit, {4} means exactly 4 times
years = re.findall(r"\s\d{4}\s", some_text)
# note the use of r before the string to indicate a raw string
# we use raw strings to avoid double escaping with \\\\ or \\n etc
# raw strings are very useful when working with regular expressions
print(years) # we could loop and trim whitespace 
# but instead we can use a more complex regular expression pattern
# we will use a capturing group to capture only the digits
years = re.findall(r"\s(\d{4})\s", some_text)
print(years) # now we only get the 4 digit years
# now you can convert to integers
# TODO explore other methods of re such as re.search, re.match, re.sub, re.split

# regular expressions are very powerful but use them wisely
# there is a saying by Jamie Zawinski - Developer of Netscape Navigator
# Some people, when confronted with a problem, think “I know, I'll use regular expressions.” 
# Now they have two problems.

# you can solve many problems with usual in, find, replace, split, strip methods

# now move onto datetime module
# somewhat confusingly there is a datetime module and a datetime class inside it
# we will import datetime class from datetime module
from datetime import datetime # otherwise we would have to use datetime.datetime
# let's get current date and time
current_time = datetime.now()
print(current_time)
# we can also format the date and time in specific ways
# for example we can use strftime method
# we can provide a format string to strftime
# %Y - 4 digit year
# %m - 2 digit month
# %d - 2 digit day
# %H - 24 hour format
# %M - minutes
# %S - seconds
# %A - full weekday name
# %B - full month name
# %p - AM/PM
# %Z - timezone
# %j - day of the year

# let's see an example
formatted_time = current_time.strftime("%H_%M:%S %Y-%m-%d ") # - is just a separator
print(formatted_time)

# now let's check math module
# it offers some mathematical functions
import math

# let's see some constants
print(math.pi)
print(math.e)
print(math.tau) # tau is 2 * pi

# some methods
print(math.sqrt(16))
print(math.pow(2, 3)) # 2^3
print(math.exp(2)) # e^2
print(math.log(10)) # ln(10)
print(math.log10(100)) # log10(100)
#sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh
print(math.sin(math.pi/2)) # sin(90 degrees) note it is in radians
# full docs of math module https://docs.python.org/3/library/math.html

# there is a random module great for generating random numbers
import random
# random.random() gives a random float between 0 and 1
print(f"Random float between 0 and 1: {random.random()}")
# some integers
print(f"Random integer between 1 and 72: {random.randint(1, 72)}")
# NOTE randint is inclusive of both ends - rare for programming languages
# if you want always to have specific random numbers you can set a seed
random.seed(42) # setting seed to 42 - any number will do
print(f"Random integer between 1 and 72: {random.randint(1, 72)}")
print(f"Random integer between 1 and 72: {random.randint(1, 72)}")
# why use seed?
# to get reproducible results
# random numbers are really pseudo random numbers - there is a repeating pattern
# this repeating patterns is very very very long - but it is there

# statistics module is useful for statistical calculations
# there is also extensive numpy and pandas libraries for more advanced statistics

# now let's explore itertools
# itertools is a module for working with iterators
# iterators are objects that can be iterated over
import itertools
# let's look at cycle
# cycle will cycle through an iterable
# we can use it to create an infinite loop
# we will use a for loop to break the infinite loop

cycle_obj = itertools.cycle([1, 2, 3]) # we can cycle through any iterable
total = 0
for i in cycle_obj:
    total += i
    print(i, total)
    if total > 1000:
        break

# https://docs.python.org/3/library/itertools.html for more itertools
# let's say we want all permutations of 3 elements
elements = "ABC"
permutations = itertools.permutations(elements)
permutations = list(permutations) # permutations is iterator so we need to convert to list
print(permutations)

# there are many modules for working with files and paths
# those we will explore when working with text files in the next lesson

# some interesting packages to explore
# sqlite3 - for working with sqlite databases
# os - for working with operating system
# turtle - for creating graphics
# tkinter - for creating GUI applications

# there are many more modules and packages in the standard library
# explore them as you need them

# chances are someone has already solved the problem you are working on