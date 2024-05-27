# Let's talk about Python dictionaries
# Official Documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Dictionaries are unordered collections of items. 
# While other compound data types have only value as an element, a dictionary has a key: value pair.
# Key idea(pun intended): with dictionaries, you can access the value using the key very quickly.(O(1) time complexity)
# In other languages, dictionaries are known as associative arrays, hashmaps or hash tables.

# Properties of Dictionary:
# 1. Dictionaries are mutable: They can be changed in place. - we can change the value of a key
# 2. Dictionaries are dynamic: They can grow and shrink as needed. - meaning we can add /remove new key-value pairs or remove existing ones
# 3. Dictionary elements are not ordered: They are stored by key, not by order of insertion.
# Note since Python 3.7 dictionaries are ordered by insertion order. - so there is some order in the dictionary
# 4. Dictionary elements are accessed via keys, not via indices. - this is important to remember
# 5. Keys must be unique in a dictionary, values don’t have to be. - if you have the same key twice, the second value will overwrite the first one
# 6. Dictionaries are iterable. - we can iterate over the keys, values or key-value pairs
# 7. Nesting of dictionaries is possible. - we can have a dictionary inside a dictionary and so on

# Creating a dictionary
empty_dict = {}  # not to be confused with f-string usage of {}
print(empty_dict)
also_empty_dict = dict() # using the dict constructor
print(also_empty_dict)

# let's see how long are our dictionaries
print(len(empty_dict))
# we can add key-value pairs to the dictionary
empty_dict["key1"] = "value1"
empty_dict["key2"] = "value2"
# print whole dictionary
print(empty_dict)
# now check the length of the dictionary
print(f"Length of the dictionary is {len(empty_dict)}")

# let's make a telephone dictionary
tel_dict = {"Valdis":2645, "Līga":2646, "Maija":2647}
# so when creating a dictionary we can use strings as keys then we use : to separate key and value
# and we separate key-value pairs with commas
# print the whole dictionary
print(tel_dict)

# usually we do not want to print the whole dictionary - we are looking for particular values by key
# let's find out Valdis' phone number
print("Valda telefons ->",tel_dict["Valdis"]) # this is going to be very fast even if I have millions of entries

# so let's TRY looking for Karlis' phone number
try:
    print("Kārļa telefons ->",tel_dict["Kārlis"])
except KeyError as ke:  # instead of ke could be any variable name such as e
    print("Kārlis nav mūsu telefona grāmatā")
    print(ke) # actual error message

# keys are case sensitive so "Valdis" is not the same as "valdis"
try:
    print("valda telefons ->",tel_dict["valdis"])
except KeyError as ke:
    print("valdis nav mūsu telefona grāmatā")
    print(ke)

# we are not forced to use try except, we have other ways of checking if key exists
# let's check if Rūta is in our phonebook
if "Rūta" in tel_dict:
    print("Rūtas telefons ->",tel_dict["Rūta"])
else:
    print("Rūta nav mūsu telefona grāmatā")

# let's add Rūta to our phonebook
tel_dict["Rūta"] = 2648
# let's check if Rūta is in our phonebook
if "Rūta" in tel_dict:
    print("Rūtas telefons ->",tel_dict["Rūta"])
else:
    print("Rūta nav mūsu telefona grāmatā")

# we also have a get method for dictionaries
# instead of tel_dict["Valdis"] we can use tel_dict.get("Valdis")
# get is great if you are not sure if the key exists
print("Valda telefons ->",tel_dict.get("Valdis"))
# now for Pēteris
print("Pētera telefons ->",tel_dict.get("Pēteris")) # this will not throw an error
# Instead None is given if key is not found
# so essentially get contains an if else statement inside
# we can also provide a default value if key is not found
print("Pētera telefons ->",tel_dict.get("Pēteris", "Nav mūsu telefona grāmatā"))

# to finish this section get is very useful when WE ARE NOT SURE if key exists

# more on adding new values to dictionary
# so syntax is dict_name[key] = value , key can be any immutable type such as string, number, tuple
# typically key is a string but it can be any immutable type

# remember that the key must be unique in the dictionary
# so let's try assign Valdis a new number
tel_dict["Valdis"] = 9000
print("Valda telefons ->",tel_dict["Valdis"]) # so the new number overwrites the old one

# as an alternative we could use a setdefault method
# idea is to set a default value if key does not exist
# so similar to
key = "Rūta"
if key not in tel_dict:
    tel_dict[key] = 2649
else:
    print(f"{key} jau ir mūsu telefona grāmatā - DOING NOTHING")
print(f"{key} telefons ->",tel_dict[key])

# instead we could use setdefault method
key = "Līga"
tel_dict.setdefault(key, 2650) # so if key exists we do nothing, if key does not exist we set the default value
print(f"{key} telefons ->",tel_dict[key])
# so now Mārtiņš will be added with default value
key = "Mārtiņš"
tel_dict.setdefault(key, 2651) # so if key exists we do nothing, if key does not exist we set the default value
print(f"{key} telefons ->",tel_dict[key])
# let's try again
tel_dict.setdefault(key, 7777) # so if key exists we do nothing, if key does not exist we set the default value
print(f"{key} telefons ->",tel_dict[key])

# so if keys must be unique, how do we handle multiple phone numbers for the same person?
# so Valdis gets second number for work, and also gets a fax number

# so we can use a list as a value
tel_dict["Valdis"] = [9000, 9001, 9002]
# so now we can access Valdis' numbers
print("Valda telefoni ->",tel_dict["Valdis"])
# full dictionary
print(tel_dict)
# so I am storing a list of numbers as values assosiated with Valdis key

# this is okay approach if all values fit neatly in a list as similar items
# but what if we have different types of values?

# better approach would be to use a dictionary as a value as well
# so Valdis has 3 numbers one for home, one for work and one for fax
# so we will use keys "home", "work", "fax" to store the numbers
tel_dict["Valdis"] = {"home":9000, "work":9001, "fax":9002}
# so now we can access Valdis' numbers
print("Valda telefoni ->",tel_dict["Valdis"])
# so we have a dictionary inside a dictionary! - this is called nesting quite normal in Python
# also later when we work with JSON data we will see that JSON data often contains nested dictionaries

# so let's see how we can access nested dictionaries
# so how about getting fax for Valdis?
print("Valda fakss ->",tel_dict["Valdis"]["fax"]) # so we first get the Valdis dictionary and then we get the fax key
# if we were not sure of either Valdis or fax key we could use get method(s)
print("Valda fakss ->",tel_dict.get("Valdis", {}).get("fax")) # so we first get the Valdis dictionary and then we get the fax 
# then if I want my summerhome phone number
print("Valda summerhome ->",tel_dict.get("Valdis", {}).get("summerhome")) # so we first get the Valdis dictionary and then we get the summerhome key
print("Valda summerhome ->",tel_dict.get("Valdis", {}).get("summerhome", "No such Number")) # so we first get the Valdis dictionary and then we get the summerhome key

# so values can be any type, even another dictionary as we've just seen
# values can be lists# 
# values can be strings
# values can be numbers

# let's print our dictionary again
print(tel_dict)

# now let's reassign Valdis same number as Līga
tel_dict["Valdis"] = tel_dict["Līga"]
# so now Valdis has the same number as Līga
# full dictionary
print(tel_dict)
# thus values can be duplicated but keys must be unique

# keys can be any immutable type so we could use emojis as keys
tel_dict["🐍"] = 1234
print(tel_dict)

# if I want to remove a key-value pair from dictionary
# I can use del keyword
del tel_dict["🐍"]
print(tel_dict)
# if I try to delete a key that does not exist I will get a KeyError
try:
    del tel_dict["🐍"]
except KeyError as ke:
    print("Key 🐍 does not exist in our phonebook")
    print(ke)

# alternative way to remove key-value pair is to use pop method
# so pop will return the value and remove the key-value pair
# if key does not exist we will get a KeyError
# let's remove Martiņš from our phonebook
print(tel_dict.pop("Mārtiņš"))
print(tel_dict)
# pop also will not throw an error if key does not exist if we provide a default value
print(tel_dict.pop("Mārtiņš", "Nav mūsu telefona grāmatā"))
# so pop is useful when we want to remove a key-value pair and get the value at the same time

# so let's go through all the keys in our dictionary with loop
for key in tel_dict:
    print(f"Key {key} has value {tel_dict[key]}")
    # we could use get but there is no need here. Why?
    print(f"Key {key} has value {tel_dict.get(key)}") # no need because we know key exists

# we will see there are other ways to loop through dictionaries
# we cold loop through both keys and values
for key, value in tel_dict.items(): # key, value are just variable names, we could use any names
    # k,v in tel_dict.items() would work just as well
    print(f"Key {key} has value {value} same as {tel_dict[key]}")
    # again no need for get method here since we KNOW key exists

# so how would we find a value in our dictionary?
# to find a value we need to loop through all the values
# this means finding value is same speed as finding value in a list
# dictionary is fast for finding values by key but slow for finding values by value

# so let's try to find a phone number
search_number = 2647
for key, value in tel_dict.items(): # we can see that we have to go through all the values
    # this is O(n) operation where n is the number of key-value pairs in the dictionary
    # same speed as finding a value in a list
    if value == search_number:
        print(f"Phone number {search_number} is for {key}")
        break


# let's write a function that returns a key by value or default key if value is not found
def get_key_by_value(my_dict, search_value, default_key="Nav atslēgas"):
    '''
    Function to find a key by value in a dictionary
    my_dict - dictionary where we are searching
    search_value - value we are looking for
    default_key - key to return if value is not found
    Returns key if value is found, default_key if value is not found
    Average Complexity: O(n) where n is the number of key-value pairs in the dictionary
    '''
    for key, value in my_dict.items():
        if value == search_value:
            return key
    # so at this step if we have not found the value we return the default key
    return default_key

# let's test our function
print(get_key_by_value(tel_dict, 2647)) # this should return Maija
# let's test with a value that does not exist
print(get_key_by_value(tel_dict, 9999)) # this should return default key

# how about getting all the keys for a value?
# we already know that values can be duplicates for different keys
# so we can have multiple keys for the same value

def get_keys_by_value(my_dict, search_value) -> list:
    '''
    Function to find all keys by value in a dictionary
    my_dict - dictionary where we are searching
    search_value - value we are looking for
    Returns list of keys if value is found, empty list if value is not found
    Average Complexity: O(n) where n is the number of key-value pairs in the dictionary
    '''
    keys = [] # create a blank list to store keys
    for key, value in my_dict.items():
        if value == search_value:
            keys.append(key)
    return keys

# let's test our function
print(get_keys_by_value(tel_dict, 2647)) # this should return ["Maija"]
# now about 2646
print(get_keys_by_value(tel_dict, 2646)) # this should return ["Līga", "Valdis"]
# let's test with a value that does not exist
print(get_keys_by_value(tel_dict, 9999)) # this should return empty list

# now I will show you how to extract keys and values separately
keys = tel_dict.keys()
print(keys) # we see this is special dictionary view object
# if we want a list we simply wrap it in list constructor
keys = list(tel_dict.keys())
print(keys) # now we have a list of keys
# this list is not connected to the dictionary so if we change the dictionary the list will not change

# similarly we can get a list of values
values = list(tel_dict.values())
print(values) # now we have a list of values
# again this list is not connected to the dictionary so if we change the dictionary the list will not change
# let's add Ede keys list
keys.append("Ede")
print(keys) # no relation to dictionary
# let's add 2 more numbers to values list
values.extend([1234, 5678])
print(values) # no relation to dictionary

# we can take two lists (any iterables actually) and create a dictionary 
new_phone_book = dict(zip(keys, values)) # so zip lets me combine two lists into a list of tuples
print(new_phone_book)
# we can see if lengths of iterables are not the same zip will stop at the shortest iterable

# we could trivially create a reversed dictionary
reversed_phone_book = dict(zip(values, keys)) 
# print length of dictionary
print("Length of reversed phone book:", len(reversed_phone_book))

# let's print the reversed phone book
print(reversed_phone_book)
# with such reverse dictionary we can quickly find a key by value
# only thing to remember is that values must be unique in the original dictionary

# we could make a function to create a reversed dictionary with provision that if value is not unique we will get a list of keys

def reverse_dict(my_dict):
    '''
    Function to reverse a dictionary
    my_dict - dictionary to reverse
    Returns reversed dictionary
    '''
    reversed_dict = {}
    for key, value in my_dict.items():
        if value in reversed_dict:
            reversed_dict[value].append(key)
        else:
            reversed_dict[value] = [key] # so we create a list with one key
    return reversed_dict

# let's test our function
reversed_tel_dict = reverse_dict(tel_dict)
print(reversed_tel_dict)
# so let's find out who is using 2646
print("2646 is used by", reversed_tel_dict[2646])

# syntax for integer keys is very similar to list syntax - well identical
# so we can use integers as keys

# so when should we use lists and when should we use dictionaries?
# especially when we have integers keys?

# if we have keys that are small or sequential integers we should use a list
# so for example if keys are say from 5 to 180 we should use a list 
# sure we lose on some memory - for example we are not using 0,1,2,3,4 indexes
# but we gain in speed - we can access list by index very quickly

# dictionary we would use when keys are not sequential or not integers
# so integers 100, 532452, -6252, 855 would be better suited are dictionary keys

# so again why should we use dictionary over list

# if we had a list of phone numbers and we wanted to find a phone number by name
# we would have to go through all the names to find the phone number
telephone_list = [["Valdis", 2645], ["Līga", 2646], ["Maija", 2647], ["Rūta", 2648]]
# so to find Rūta's phone number we would have to go through all the names
search_name = "Rūta"
for name, number in telephone_list: # I am unpacking the internal lists
    if name == search_name:
        print(f"Phone number for {search_name} is {number}")
        break

# without unpacking
for person in telephone_list:
    if person[0] == search_name:
        print(f"Phone number for {search_name} is {person[1]}")
        break

# much faster and nicer is to use a dictionary
# so we can find a phone number by name very quickly
print(f"Phone number for {search_name} is {tel_dict[search_name]}")# so instead of O(n) we have O(1) operation

# let's see how we can update a dictionary with another dictionary
new_person_dict = {"Kārlis": 2650, "Liene": 2651, "Maija": 2652}
# so we can update our dictionary with new_person_dict
print(f"BEFORE update {tel_dict}")
tel_dict.update(new_person_dict)
print(f"AFTER update {tel_dict}")
# so we see that update will overwrite values for existing keys and add new key-value pairs

# now we get to same issue that lists have with =
# = for mutable structures will simply be a reference to the same structure - an alias
# so if we change the new_person_dict we will change the tel_dict as well

tel_dict_alias = tel_dict # no copy is done just a reference
print(tel_dict_alias)
# let's change the alias
tel_dict_alias["Kārlis"] = 2655
# let's add one more
tel_dict_alias["Uldis"] = 2656
print(tel_dict_alias)
# let's see the original dictionary
print(tel_dict) # so we see that tel_dict has changed as well

# so to copy we use copy method
tel_dict_copy = tel_dict.copy()
print(tel_dict_copy)
# let's change the copy
tel_dict_copy["Toms"] = 2657
print("COPIED TELE BOOK", tel_dict_copy)
# let's see the original dictionary
print("ORIGINAL", tel_dict) # so we see that tel_dict has not changed

# now how about saving the phone book to a file?
# we could save it to a text file but we will work with text later
# easy way would be to use pickle module
import pickle
# so we can save our dictionary to a file
with open("phonebook.pickle", "wb") as f:
    pickle.dump(tel_dict, f)
# we will have a separate lecture on pickle module and working with text files

# we could have saved our dictionary as JSON as well 
# with JSON we could edit the text file with any text editor
# and JSON is a standard format for data exchanges