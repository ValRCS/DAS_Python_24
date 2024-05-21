## Let's talk about Python dictionaries
## Official documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## main idea - key-value pairs where key is unique and value can be anything
# Other languages call them associative arrays, hashmaps, hash tables, etc.
## Main idea we have O(1) time complexity for searching, inserting, deleting
# O(1) means that no matter how many elements we have in the dictionary, 
# we can find the value by key in the same time

# Properties:
# Mutable - we can change the values
# Dynamic - we can add or remove elements meaning keys and corresponding values
# Unordered - we cannot rely on the order of the elements
# Since Python 3.7 dictionaries are ordered by insertion order - we do not reorganize them
# Keys must be immutable - strings, numbers, tuples - so no lists for one
# Values can be anything - lists, dictionaries, functions, etc.
# Iterables - we can iterate over dictionary keys or values or key-value pairs
# Nesting - we can have dictionaries inside dictionaries and so on

## let's make an empty dictionary
my_dict={} # so in Python we use curly braces to define dictionaries - note not related to f-strings using {}
print(my_dict) # {}
# also we could use dict() constructor
also_empty_dict=dict() # so this is reason why we do not call variables dict !
# again do not use the build in names for variables
# full built in names list: https://docs.python.org/3/library/functions.html
print(also_empty_dict) # {}

# how big is our dictionary?
print(f"Size of my_dict: {len(my_dict)}") # 0
# we could check the type of the variable
print(f"Type of my_dict: {type(my_dict)}") # <class 'dict'>

# let's create a dictionary with some prebuilt key-value pairs
tel_dict = {"valdis":2640, "līga":2911, "pēteris":2912}	
# so we use : to separate key and value and , to separate key-value pairs
print(tel_dict) # {'valdis': 2640, 'līga': 2911, 'pēteris': 2912}

# so let's find out Valdis' phone number
print("valdis phone number", tel_dict["valdis"]) # 2640 # so this operation is in O(1) time - very quick no matter how big the dictionary is
# let's try to find someone who is not in the dictionary
try:
    print("karlis phone number", tel_dict["karlis"]) # KeyError: 'karlis' # so we get an error
except KeyError as e:
    print("karlis not found in the dictionary")

# note that keys are case sensitive
# Valdis is also not in the dictionary
try:
    print("Valdis phone number", tel_dict["Valdis"]) # KeyError: 'Valdis' # so we get an error
except KeyError as e:
    print("Valdis not found in the dictionary")

# we can also check if key is in the dictionary
print("valdis is in the dictionary?", "valdis" in tel_dict) # True
print("Valdis is in the dictionary?", "Valdis" in tel_dict) # False

# we can also add new entries to the dictionary
# let's add Maija to the dictionary
tel_dict["maija"]=2913 # will overwrite value for maija if it exists
print(tel_dict) # {'valdis': 2640, 'līga': 2911, 'pēteris': 2912, 'maija': 2913}

# so if I want to update the value for Valdis
tel_dict["valdis"]=2641 # will overwrite value for valdis
print(tel_dict) # {'valdis': 2641, 'līga': 2911, 'pēteris': 2912, 'maija': 2913}

# so this means that keys have to be unique - case sensitive
# of course I could add number for Valdis 
tel_dict["Valdis"]=2642 # so this is different key
print(tel_dict) # {'valdis': 2641, 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642}

# what do we do if we want to store more than one value for a key?
# one approach is to store a list of values
# so let's say valdis has 3 phone numbers now
tel_dict["valdis"]=[2641,2642,2643] # so we store a list of phone numbers
print(tel_dict) # {'valdis': [2641, 2642, 2643], 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642}

# so how would I get the last phone number for Valdis?
# this would be a two step approach
# first we could get the full list of phone numbers
valdis_phones=tel_dict["valdis"] # i do not need the variable name to be the same as the key
# if i wanted a copy here I would use valdis_phones=tel_dict["valdis"].copy() then they are different lists
# so valdis_phones is an alias actually to the list stored in the dictionary
print(f"Valdis phone numbers: {valdis_phones}") # Valdis phone numbers: [2641, 2642, 2643]
print(f"Last Valdis phone number: {valdis_phones[-1]}") # Last Valdis phone number: 2643

# so what if I want to add a new phone number to Valdis?
valdis_phones.append(2644) # so we use the append method to add a new element to the list
print(f"Valdis phone numbers: {valdis_phones}") # Valdis phone numbers: [2641, 2642, 2643, 2644]
# now let's check our dictionary
print(tel_dict) # {'valdis': [2641, 2642, 2643, 2644], 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642}
# i could have skipped the variable and added the value directly to the list
tel_dict["valdis"].append(2645) # so this is a bit shorter but less readable
print(tel_dict) # {'valdis': [2641, 2642, 2643, 2644, 2645], 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642}
# also our valdis_phones variable is still pointing to the same list
print(f"Valdis phone numbers: {valdis_phones}") # Valdis phone numbers: [2641, 2642, 2643, 2644, 2645]
# ok let's go back to single number let's take third number
print(f"valdis third phone number: {tel_dict['valdis'][2]}") # valdis third phone number: 2643
tel_dict["valdis"]=tel_dict["valdis"][2] # so we overwrite the list with the third phone number
print(tel_dict) # {'valdis': 2643, 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642}

# keys can be in any unicode characters
# so let's say we want to store some emojis
tel_dict["👩"]=2914
print(tel_dict) # {'valdis': 2643, 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642, '👩': 2914}
# of course we can use Latvian letters
tel_dict["āris"]=2915
print(tel_dict) # {'valdis': 2643, 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642, '👩': 2914, 'āris': 2915}

# we could maybe want to extract all keys
print(tel_dict.keys()) # dict_keys(['valdis', 'līga', 'pēteris', 'maija', 'Valdis', '👩', 'āris'])
# maybe we want to convert them to list
key_list = list(tel_dict.keys()) # this will be copy!
print(key_list) # ['valdis', 'līga', 'pēteris', 'maija', 'Valdis', '👩', 'āris']
# similarly values
print(tel_dict.values()) # dict_values([2643, 2911, 2912, 2913, 2642, 2914, 2915])
# and we can convert them to list
value_list = list(tel_dict.values()) # this will be copy!
print(value_list) # [2643, 2911, 2912, 2913, 2642, 2914, 2915]

# let's change first value to 2911 as well
value_list[0]=2911
print(value_list) # [2911, 2911, 2912, 2913, 2642, 2914, 2915]

# let's get rid of āris in the key_list
# simplest would be to pop the key (again it is just a list)
key_list.pop() # so we remove the last element , i am not saving it
print(key_list) # ['valdis', 'līga', 'pēteris', 'maija', 'Valdis', '👩']

# we can make a new dictionary from two lists(iterables)
new_dict=dict(zip(key_list,value_list)) # so we zip the two lists together and then convert them to dictionary
print(new_dict) # {'valdis': 2911, 'līga': 2911, 'pēteris': 2912, 'maija': 2913, 'Valdis': 2642, '👩': 2914}
# what happened to āris? he is not key_list anymore, then the last value was not applied
# print lengths of all three
print(f"Length of key_list: {len(key_list)}") # 6
print(f"Length of value_list: {len(value_list)}") # 7
print(f"Length of new_dict: {len(new_dict)}") # 6
# so therefore zip stops at the shortest list

# of course we could use value_list as keys and key_list as values
reversed_dict = dict(zip(value_list,key_list)) # so we zip the two lists together and then convert them to dictionary
print(reversed_dict) # {2911: 'līga', 2912: 'pēteris', 2913: 'maija', 2642: 'Valdis', 2914: '👩'}
# note that we lost also valdis because value of līga was overwritten

# thus if we want to reverse a dictionary we could do this
reversed_dict = dict(zip(tel_dict.values(),tel_dict.keys())) # so we zip the two lists together and then convert them to dictionary
print(reversed_dict) 

# how do we use this reversed dictionary?
# assuming we know the phone number we can find the name
# let's say we know the phone number 2913
print(f"Name for phone number 2913: {reversed_dict[2913]}") # Name for phone number 2913: maija

# so when should you use numeric keys and not lists?

# when int keys ar sparse and spread over a wide range then we use dictionary

# if we have numbers very close together and starting around 0 then we can use list

# we do not have to use two lists to create a dictionary
# we could use any two iterables
char_dict = dict(zip("Valdis",range(1,9000))) # so we zip the two lists together and then convert them to dictionary
# note that zip will stop when Valdis is over
print(char_dict) # {'V': 1, 'a': 2, 'l': 3, 'd': 4, 'i': 5, 's': 6}

# i could even create number dictionary from two ranges
num_dict = dict(zip(range(100,110),range(2011,2200))) # so we zip the two lists together and then convert them to dictionary
print(num_dict) # {100: 2011, 101: 2012, 102: 2013, 103: 2014, 104: 2015, 105: 2016, 106: 2017, 107: 2018, 108: 2019, 109: 2020}

# most often keys are strings but they can be numbers as well

# let's say we want to store some data about people
# we could use a dictionary
# let's say we want to store names, ages, and phone numbers
people_dict = {"Valdis":{"age":55,"phone":2643},"Līga":{"age":50,"phone":2911},"Pēteris":{"age":30,"phone":2912}}
# this would be a nested dictionary

# how would I get my phone number?
print(f"My phone number: {people_dict['Valdis']['phone']}") # My phone number: 2643


# let's loop through our phone number dictionary
for key in tel_dict: # we are guaranteed to get all keys, key is just a variable name, could k or x or anything
    print(f"Key: {key} -> Value: {tel_dict[key]}") # so we loop through all keys and print key and value

# longer way would be to write tel_dict.keys() but it is not necessary
for key in tel_dict.keys(): # we are guaranteed to get all keys, key is just a variable name, could k or x or anything
    print(f"Key: {key} -> Value: {tel_dict[key]}") # so we loop through all keys and print key and value

# if I know that I need both key and value I can use items() method

for key, value in tel_dict.items(): # we are guaranteed to get all key-value pairs, we could use k,v or name,phone or anything
    print(f"Key: {key} -> Value: {value} same as {tel_dict[key]}") # so we loop through all key-value pairs and print key and value