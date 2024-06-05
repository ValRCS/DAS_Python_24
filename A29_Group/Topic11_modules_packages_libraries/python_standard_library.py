# Python Standard Libary is a collection of modules that come with Python automatically
# no matter where you install Python

# to use them simply import them
# you could use aliases as well if you want to type less

# full list of Python Standard Library modules
# https://docs.python.org/3/library/index.html

# let's look at few examples
# https://docs.python.org/3/library/string.html
# string is simply a collection of constants and functions that work with strings
import string
print(string.ascii_letters)
# it can be useful to avoid typos
# punctuation is a string constant
print(string.punctuation)

# re is a regular expression module
# https://docs.python.org/3/library/re.html
import re
text = "In 1984 a quick brown fox jumps over a lazy fox in 2024 Rīga not 900 BC and not 90000 AD"
# we can search for specific words
# we can search for specific patterns
# how would we search for year numbers in the text?

# I recommend using site such as https://regex101.com to test your regular expressions

# so let's find all year numbers in the text
# years are defined as 4 digits in a row enclosed in spaces
# we do not want to capture spaces
# we want to capture only the year numbers
# we can use findall function

years = re.findall(r"\b\d{4}\b", text) # note use of r for raw string
# it is more convenient to use raw strings for regular expressions
# because we do not need to escape backslashes
print(years) # of course years will be strings but you can convert them to int you know that

# there is datetime module for working with dates and times
# https://docs.python.org/3/library/datetime.html
# usually we want datetime class from datetime module
from datetime import datetime # this is a bit of strange design for this module
now = datetime.now()
print(now)
print(now.year)
# you can format years etc. as you like

# there are math, statistics, random modules for math operations
# https://docs.python.org/3/library/math.html
# https://docs.python.org/3/library/statistics.html
# https://docs.python.org/3/library/random.html
# so random number from 1 to 10
import random
print(random.randint(1,10)) # note that randint is inclusive ! rare for functions in Python

# there are interseting itertools and functools modules
# for example product from itertools
# https://docs.python.org/3/library/itertools.html

from itertools import product
# let's say we have two iterables
name = "Valdis"
numbers = [1,2,3,4]
# we can create all possible combinations of the two
# we can use product function
combinations = list(product(name, numbers))
print(combinations)
# we could have used two nested loops to achieve the same result but this is cooler


# so we can see that Python Standard Library is quite extensive
# explore it yourself and use it in your projects
