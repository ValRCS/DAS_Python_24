# 1a. Uzrakstīt funkciju: get_char_count(text), kas saņem string un izvada
# vārdnīcu ar atsevišķu burtu lietojumu skaitu.
# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1}
# vārdnīcas secībai nav nozīme, un visam alfabetam nav jābut

def get_char_count(text, convert_keys_to_int=False):
    # if we expect number simply cast to str 
    text = str(text) # if text is already string nothing will happen
    cc = {} # start a blank dictionary
    for t in text: # so we loop through all characters in the text
        if t in cc: # if we find an existing character we increment the count
            cc[t] += 1 # constant time operation
        else: # we have not seen this character before so we start the count at 1
            cc[t] = 1 # this is also constant time operation
    # print(cc)
    # could try converting all keys to int if flag is set
    if convert_keys_to_int:
        for key in list(cc.keys()):
            try:               
                # cc[int(key)] = cc.pop(key) # will not work as intended
                # above will always pop but not always add new key
                cc[int(key)] = cc[key]
                cc.pop(key) # we only do this if we successfully added new key
            except ValueError:
                pass

    return cc
        
character_count_dict = get_char_count('hubba bubba')
print(character_count_dict)
# we could print immediately as well
print(get_char_count('abracadabra maģija mana'))
digit_count = get_char_count(900053521)
print(digit_count)
# we could convert all keys to int
print(get_char_count(900053521, convert_keys_to_int=True))
# we could convert all keys to int
print(get_char_count("abracadabra", convert_keys_to_int=True))

# there is an inefficient solution which uses count method for strings

def get_char_count_suboptimal(text):
    cc = {} # start a blank dictionary
    for t in text: # so we loop through all characters in the text
        cc[t] = text.count(t) # this is not efficient for long texts
        # why because count has to go through the whole text each time
    return cc

# above works but not efficient O(n^2) complexity - quadratic

# there is also a solution with built in Counter class

from collections import Counter # standard library
my_counter = Counter('abracadabra')
print(my_counter)
# I call this object a dictionary "with benefits"
print(my_counter.most_common(3)) # so I can get most common items
print(my_counter['a']) # so I can get count of a
# so counter type works like a dictionary but has additional methods

foods = ['apple', 'banana', 'orange', 'kiwi', 'blueberry', 'potatoes', 
         'apple', 'banana', 'banana']

food_counter = Counter(foods)
print(food_counter)