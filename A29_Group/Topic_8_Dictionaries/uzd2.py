# 2. Vārdnīcu labotājs
 
# Uzrakstīt replace_dict_value(d, bad_val, good_val), kas atgriež vārdnīcu ar nomainītām vērtībām
 
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtības bad_val kura jānomaina uz good_val
 
# clean_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10} , jo 5 bija vērtība, kas jānomaina.
 
def replace_dict_value(d, bad_val, good_val):
    """
    Replace bad_val with good_val in dictionary d
    IN PLACE - modifies the dictionary
    INPUT: 
    d - dictionary, 
    bad_val - value to be replaced, 
    good_val - value to replace with
    OUTPUT:
    dictionary with replaced values
    """
    for key, val in d.items():
        if val == bad_val:
            d[key] = good_val
    return d

some_dict = {'a':5,'b':6,'c':5, 'd': 900}
result = replace_dict_value(some_dict, 5, 10)
# now the question is what will be the result? and what will be some_dict?
print(result)
# how about some_dict?
print(some_dict)

# if we want to preserve the original dictionary we can create a copy
# and then modify the copy
def replace_dict_value_out_of_place(d, bad_val, good_val):
    """
    Replace bad_val with good_val in dictionary d
    INPUT: 
    d - dictionary, 
    bad_val - value to be replaced, 
    good_val - value to replace with
    OUTPUT:
    dictionary with replaced values
    """
    d = d.copy() # create a copy of the dictionary
    # now outside dictionary will not be modified
    for key, val in d.items():
        if val == bad_val:
            d[key] = good_val
    return d

some_dict = {'a':5,'b':6,'c':5, 'd': 900}
result = replace_dict_value_out_of_place(some_dict, 5, 10)
# now the question is what will be the result? and what will be some_dict?
print(result)
# how about some_dict?
print(some_dict)