# 1.uzd.  Simbolu biežums
 
# def get_char_count(text):
#     count_characters = {char: text.count(char) for char in text}
#     return count_characters

# let's write above solution that uses count without dictionary comprehension
# def get_char_count(text):
#     count_characters = {}
#     for char in text:
#         count_characters[char] = text.count(char) # count is linear time complexity
#     return count_characters

# instead a more optimal solution would be to iterate over the text only once


def get_char_count(text):
    # if we want to support digits
    # we simply typecast the text to string
    text = str(text) # if text is already string this will do nothing
    char_dict={}
    for char in text: # for dictionaries this is also constant time complexity O(1)
        if char in char_dict:
            char_dict[char] += 1
        else: # we set key value to 1 if it's not in the dictionary
            char_dict[char] = 1
    return char_dict
 
 
result = get_char_count("hubba bubba")
print(result)
# let's try some numbers
result = get_char_count(3252000435531123456789)
print(result)

# let's try a pure digit counter for integers
def pure_digit_counter(number):
    # assuming number is an integer!
    # TODO add check if number is integer
    # we will store results in a list
    # we will simply divide the number by 10 and get the remainder
    # this will give us the last digit
    # we will then divide the number by 10 and repeat the process
    # until the number is zero
    # this will give us the digits in reverse order

    # set digit_count to 0 for all 10 digits
    digit_count = [0]*10 
    while number > 0:
        digit = number % 10 # find last digit
        digit_count[digit] += 1
        number = number // 10
    # let's transform list to dictionary
    digit_count = {i: digit_count[i] for i in range(10)}
    return digit_count

result = pure_digit_counter(32520004355311203456789)
print(result)

# Python actually offers a built in function to count digits
# we can use collections.Counter
from collections import Counter
# let's count hubba bubba
result = Counter("hubba bubba")
print(result)
# so Counter is actually a dictionary "with benefits"
# we can get top 3 most common characters
print(result.most_common(3))