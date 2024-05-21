
# 3a
def replace_dict_value_in_place(d, bad_val, good_val):
    '''
    IN PLACE function to replace bad_val with good_val in dictionary d
    d - dictionary to be modified
    bad_val - value to be replaced
    good_val - value to replace bad_val with
    '''

    for key, val in d.items():
        if val==bad_val:
            d[key]=good_val

    return(d)

print(replace_dict_value_in_place({'a':5,'b':6,'c':5}, 5, 10))

some_dict = {'a':5,'b':6,'c':5, 'd':7}
some_dict_alias = replace_dict_value_in_place(some_dict, 5, 10)
print(some_dict)
print(some_dict_alias)

# we could have done this with dictionary comprehension
def replace_dict_value(d, bad_val, good_val):
    '''
    OUT OF PLACE function to replace bad_val with good_val in dictionary d
    d - dictionary to be modified
    bad_val - value to be replaced
    good_val - value to replace bad_val with
    '''
    return {key: good_val if val==bad_val else val for key, val in d.items()}
# not very readable it is using ternary operator
# ternary operator is a compact way to write if else statements
# value = a if condition else b # similar to value = condition ? a : b in C like languages

# we could have done OUT OF PLACE without dictionary comprehension
def replace_dict_value_no_comprehension(d, bad_val, good_val):
    '''
    OUT OF PLACE function to replace bad_val with good_val in dictionary d
    d - dictionary to be modified
    bad_val - value to be replaced
    good_val - value to replace bad_val with
    '''
    new_dict = {}
    for key, val in d.items():
        if val==bad_val:
            new_dict[key]=good_val
        else:
            new_dict[key]=val
    return new_dict

# let's test these functions
print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))
print(replace_dict_value_no_comprehension({'a':5,'b':6,'c':5}, 5, 10))