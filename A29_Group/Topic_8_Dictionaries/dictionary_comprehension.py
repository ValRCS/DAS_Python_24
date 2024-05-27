# similarly how we have a list comprehension, we can also have a dictionary comprehension

# dictionary comprehension is a concise way to create dictionaries from ANY iterable

# syntax:
# {key: value for (key, value) in iterable}

# with dictionary comprehension, we can create a dictionary by filtering from existing dictionaries

# first let's create a dictionary from string and its unicode values
name = "Līga"
unicode_dict = {char: ord(char) for char in name}
print(unicode_dict)
# now I could find all characters that are not ASCII
non_ascii = {char: code for char, code in unicode_dict.items() if code > 127}
print(non_ascii)

# above operations can be done with a for loop, but dictionary comprehension is more concise
# let's see for loop examples for both
also_unicode_dict = {}
for char in name:
    also_unicode_dict[char] = ord(char)
    # note how there is not much problem if we have same character multiple times
    # we will always get same value for same key
print(also_unicode_dict)
# now we could filter out non-ASCII characters
also_non_ascii = {}
for char, code in also_unicode_dict.items():
    if code > 127:
        also_non_ascii[char] = code
print(also_non_ascii)