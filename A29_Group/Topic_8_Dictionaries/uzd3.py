# 3. Vārdnīcu tīrītājs
# 3.a  Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val no kuras jāatbrīvojas kopā ar ar tās atslēgu.
# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.
# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.
# PS. Tīram mēs are del d['a'] protams tikai tad ja atslēga 'a' eksistē.

# we will use two different approaches to solve this problem
# one will be IN PLACE and the other OUT OF PLACE

# IN PLACE
# with in place we will be iterating over the dictionary and removing the keys that have the bad value
# we have to be very careful when we are modifying the dictionary while iterating over it
# so for in place solution we would have to iterate over a copy of the keys or key,value pairs

def clean_dict_value_in_place(d, bad_val):
    for key, val in d.copy().items(): # for large dictionaries this is not efficient
        if val == bad_val:
            del d[key] # then also the value is removed as well along with the key
    return d # this will be the original (modified) dictionary

my_dict = {'a':5,'b':6,'c':5, 'd': 900}
result = clean_dict_value_in_place(my_dict, 5)
print(result)
# see that original dictionary is modified since we are modifying the dictionary in place
print("ORIGINAL",my_dict)

# OUT OF PLACE - means we will build a new dictionary from ground up
# we will not modify the original dictionary
# we will have two ways of solving this out of place 
# one would use a regular loop and the other would use dictionary comprehension

def clean_dict_value_out_of_place_loop(d, bad_val):
    new_d = {}
    for key, val in d.items():
        if val != bad_val: # so if value is not bad we add key value pair to the new dictionary
            new_d[key] = val
    return new_d

original_dict = {'a':5,'b':6,'c':5, 'd': 900}
result = clean_dict_value_out_of_place_loop(original_dict, 5)
print(result)
# see that original dictionary is not modified since we are not modifying the original dictionary
print("ORIGINAL",original_dict)

# OUT OF PLACE - dictionary comprehension
def clean_dict_value_out_of_place_comprehension(d, bad_val):
    return {key:val for key, val in d.items() if val != bad_val}

result = clean_dict_value_out_of_place_comprehension(original_dict, 5)
print(result)
print("ORIGINAL",original_dict)

# we do not have to provide original key and value pairs in the dictionary
# let's show an example that modifies both key to upper and value * 10
def clean_dict_value_out_of_place_transform(d, bad_val):
    return {key.upper():val*10 for key, val in d.items() if val != bad_val} 

result = clean_dict_value_out_of_place_transform(original_dict, 5)
print(result)
print("ORIGINAL",original_dict)

# I am not forced to use key in key transformation
# and I am not forced to use value in value transformation

# for example I could initialize a dictionary to all 0 values
text = "Valdissss Sau 2024 gads!"
my_dict = {c:0 for c in text if c.isalpha()}
print(my_dict)

# now let's solve 3.b where we have to remove multiple values
def clean_dict_values_out_of_place(d, bad_value_list): # techniclly bad_value_list could be a range,set,string,tuple as well
    return {key:val for key, val in d.items() if val not in bad_value_list}

original_dict = {'a':5,'b':6,'c':5, 'd': 900, 'e': 6}
# we want to remove 5 and 6 values
result = clean_dict_values_out_of_place(original_dict, range(1,300))
print(result)
print("ORIGINAL",original_dict)

# lets write the last function with loops without dictionary comprehension
def clean_dict_values_out_of_place_loop(d, bad_value_list):
    new_d = {}
    for key, val in d.items():
        if val not in bad_value_list:
            new_d[key] = val
    return new_d

original_dict = {'a':5,'b':6,'c':5, 'd': 900, 'e': 6}
# we want to remove 5 and 6 values
result = clean_dict_values_out_of_place_loop(original_dict, [2,4,5,6])
print(result)
print("ORIGINAL",original_dict)