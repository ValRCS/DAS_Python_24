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
