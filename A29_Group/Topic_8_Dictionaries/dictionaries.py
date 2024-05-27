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

