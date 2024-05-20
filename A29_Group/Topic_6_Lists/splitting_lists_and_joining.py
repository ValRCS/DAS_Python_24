# when working with strings it can be handy to split them into lists or join lists into strings

# Splitting strings into lists
sentence = "A quick brown fox jumps over the  \t  lazy dog"
print(sentence)
# we can use string split method to split string into list of words
words = sentence.split() # by default split uses ANY whitespace (including newlines) to split
print(words)

# now I could change some word say fox to bear
# first let's find index of fox
fox_index = words.index("fox") # rememer this could fail if "fox" is not in the list
# now let's change fox to bear
words[fox_index] = "bear"
print(words)

# So how do we create a new string from list of words?
# lists have a join method which takes an iterable of strings and joins them into a single string
# so we can join list of words into a single string
new_sentence = " ".join(words) # we join with single space
print(new_sentence)

# so we deconstructed a string into a list of words and then reconstructed it back into a string
# note that we lost the original whitespace between words, usually that is not a problem

# we could split on any character
# let's say we have a comma separated values string
csv = "Valdis, 21, 180, 80.76"
print(csv)
csv_list = csv.split(",") # we split on comma
print(csv_list)
# if we want to convert this into a list of integers when possible
# csv_list = [int(item) if item.isdigit() else item for item in csv_list] # list comprehension example
# simpler but more wordy would be to use a loop
new_list = []
for item in csv_list:
    item = item.strip() # we remove any leading or trailing whitespace from each item
    # note we are not affecting the original csv_list
    # if item.isdigit():
    #     new_list.append(int(item))
    # we could also try to convert to float
    try:
        new_list.append(float(item))
    except ValueError:
        # could add original
        print(f"Could not convert {item} to float")
        # new_list.append(item)
    # else: # if I want to keep original strings or something else
    #     new_list.append(item)

print(new_list)

# if I wanted to divide every value by 100 I could do this
new_values = []
for value in new_list:
    # new_values.append(value / 100) # could add rounding here
    new_values.append(round(value / 100, 2)) # rounding to 2 decimal places

print(new_values)

# let's say we need to convert this list of numbers into a string
new_string = str(new_values) # will not be what we want most likely
print(new_string) # simply shows string with list brackets, which is not very useful
# instead we would need to convert each number into a string and then join them
# we could use list comprehension for this
new_string = ",🍺 ".join([str(value) for value in new_values])
print(new_string)
# without list comprehension
str_list = []
for value in new_values:
    str_list.append(str(value)) # we can ALWAYS use str() to convert any value to string
new_string = ", ".join(str_list)
print(new_string)

# more resoures on split and join
# https://www.geeksforgeeks.org/python-string-split/
# real python on split and join
# https://realpython.com/python-string-split-concatenate-join/