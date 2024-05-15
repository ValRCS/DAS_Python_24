# let's talk about strings in Python

# Strings are a sequence of characters 
# Python actually does not have a character data type, a single character is a string of length 1
# Strings are immutable, meaning you cannot change them in place
# Strings can be indexed and sliced

# Strings can be created with single, double or triple quotes
food = 'kartupelis'
print(food)

# Strings can be create with double quotes
drink = "alus"
print(f"I like to drink {drink} responsibly")

# In Python there is no difference between single and double quotes
# some languages require you to use single quotes for characters and double quotes for strings

# When can this be useful?
# When you have a string that contains a single quote
# You can use double quotes to create the string
# and vice versa

text = "I'm a string with a single quote"
print(text)
also_text = 'I am a string with a "double quote"'
print(also_text)

# if I did not have the option to use double quotes
# I would have to use so called escape characters
# escape characters are used to escape the special meaning of a character

# Python escape characters
# \' - single quote
# \" - double quote
# \\ - backslash - we will see a single backslash in the next example
# \n - new line
# \t - tab
# there are some others less used ones
# full list: https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences

# let's see an example
text = 'I\'m a string with a single backslach \\ single quote and also newline\n and a tab\t with some text'
print(text)

# for longer texts we actually have a better option
# triple quotes
# triple quotes can be used to create multiline strings with no need to escape characters
# triple quotes can be single or double quotes
big_long_text = '''This is a big long text
with multiple lines
and no need to escape characters
I can quote " and ' without any problems
I can use single backslash \
'''
print(big_long_text)

# we can use f-strings to format our text

name = "Valdis"
age = 900
# f-string is a string that has f in front of it
# inside the string we can use {} to insert variables
# we can also do some formatting inside the {}
# we can also call functions inside the {}
print(f"My name is {name} and I am {age} years old")

PI = 3.14159265359
# we can format numbers inside our f-strings without affecting the original variable
# we can round the number to a certain number of decimal places
print(f"PI is {PI:.2f}")
print(f"PI is {PI:.3f}")
print(f"PI is {PI:.4f}")
# we can padd the number with zeros
print(f"PI is {PI:010.4f}")
# we can pad empty spaces as well
print(f"PI is {PI:10.4f}")
# more on f-strings: https://realpython.com/python-f-strings/
# official docs: https://docs.python.org/3/reference/lexical_analysis.html#f-strings

# we can use f-strings inside triple quotes
big_text = f'''This is a big long text
with multiple lines with variables like {name}
and no need to escape characters
I can quote " and ' without any problems
I can use single backslash \
I can put results of calculations like {age * 2}
'''
print(big_text)

# let's talk about indexing and slicing
# strings are sequences of characters
# sequences are indexed
# for indexing we use square brackets []
# indexing starts at 0

# first letter of food
print("First letter is", food[0])
# then second letter would have index 1
print(f"Second letter is {food[1]}")
# third letter would have index 2
print(f"Third letter is {food[2]}")

# how would we get the last letter of the string?
# one idea is to use length
# for now I know kartupelis has 10 letters
# so the last letter would have index 9
print(f"Last letter is {food[9]}")
# however in general we do not know the length of the string
# so we could find the length of the string
length = len(food) # len is a built-in function that returns the length of a sequence
print(f"Length of food is {length}")
# and then subtract 1 to get the last letter
print(f"Last letter is {food[length - 1]}")
# instead of doing this we can use negative indexing
# negative indexing starts from the end of the string
# last letter would have index -1
print(f"Last letter is {food[-1]}")
# second to last letter would have index -2
print(f"Second to last letter is {food[-2]}")

# see Google Developer Python Strings for more examples
# https://developers.google.com/edu/python/strings

# what happens if we try to get an index that does not exist?
# we get an IndexError
try: # we could have also checked if the index is less than the length of the string
    print(food[10]) # there is no 11th character in kartupelis !
except IndexError as e:  # as e lets us access the exception object and see the problem
    print("We got an IndexError", e)

# negative indexing also could produce this error
try:
    print("-10th character", food[-10]) # there is -10th character in kartupelis ! THIS LINE SHOULD RUN
    print(food[-11]) # there is no -11th character in kartupelis !
except IndexError as e:
    print("We got an IndexError", e)


# let's get more than one letter at a time
# we can slice strings
# so the next best thing since sliced bread is sliced strings
# in slicing we use square brackets [] and a colon :
# let's get the first 3 letters of food
# we could use food[0:3] but 0 is the default start
print(f"First 3 letters are {food[:3]}")
# technically we are getting letters from index 0 to index 2 (3 is not included)
# similarly we could get the last 3 letters
print(f"Last 3 letters are {food[-3:]}")
# how about the middle
# we could get letters from index 3 to index 6
print(f"Middle letters are {food[3:7]}")
# we could overlap the slices
# we could get letters from index 3 to index 5
print(f"Middle letters are {food[3:6]}")
# since strings are immutable we could create a new string from two slices of the same string
new_food = food[:3] + food[-3:]
print(f"New food is {new_food}")
# indexes could overlap
new_food = food[:7] + food[-5:]
print(f"New food is {new_food}")

# string slicing syntax actually has a third parameter - step
# we could get every second letter of alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"Full alphabet is {alphabet}")
print(f"Every second letter of alphabet is {alphabet[::2]}")  # ::2 means start from beginning, go to end, step 2
# we could get every third letter of alphabet
print(f"Every third letter of alphabet is {alphabet[::3]}")
# we could start from 2nd letter and get every 2nd letter
print(f"Every second letter of alphabet starting from b is {alphabet[1::2]}")
# we could stop in the middle
middle = len(alphabet) // 2 # // is integer division
print(f"Middle index is {middle}")
print(f"First half of alphabet is {alphabet[:middle]}")
# every 2nd letter starting from b and stopping in the middle
print(f"Every second letter of alphabet starting from b and stopping in the middle is {alphabet[1:middle:2]}")