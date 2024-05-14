# Python has a neat way of converting strings to lists and vice versa.

# let's say I have a sentence
sentence = "I like to eat\napples and      \n  bananas"
print(sentence)
# I want to convert this sentence to a list of words
words = sentence.split() # split by ANY whitespace by default
print(words)
# i can put the words back into a string
new_sentence = ' '.join(words)# join with space ' ' between words could be any string
# words list have to be all strings
print(new_sentence)

# let's say I have some numbers in a string separated by commas
numbers = "1,2,3,4,5,6,7,8,9,10"
print(numbers)
# I want to convert this string to a list of numbers
number_list = numbers.split(',') # split by comma
print(number_list)
# I would like to calculate the sum of these numbers how would I do that?
# print(sum(number_list)) # this will not work because we have strings

# i need to convert all the strings to numbers
# we could use a for loop
sum_numbers = 0
int_list = []
for number in number_list:
    # sum_numbers += int(number) # we could add try in case the conversion fails
    try:
        int_list.append(int(number)) # so this int could fail
        sum_numbers += int_list[-1]
    except ValueError:
        print(f"Could not convert {number} to number")
print(sum_numbers)
print(int_list)

# we could use list comprehension
also_int_list = [int(number) for number in number_list] # no try catch here
print(also_int_list)
# sum
print(sum(also_int_list))