# 2. Kopējie Elementi
def get_common_elements(seq1,seq2,seq3):
    result = set(seq1) & set(seq2) & set(seq3)
    return tuple(result)
 
result_2a = get_common_elements("abc",['a','b'],('b','c'))
print(result_2a)

# let us do this function with unlimited number of sequences
def get_common_elements_unlimited(*args):
    if not args:
        return () # default for no arguments
    # here we know for sure that at least one argument is present
    result = set(args[0]) # crucial to start with first set NOT empty set
    # for needed amount of arguments
    # if only one argument is passed then loop will be skipped
    # so I want to loop starting from 2nd argument
    for seq in args[1:]: # remember that slicing does not give error if out of bounds
        result &= set(seq) # same as result = result & set(seq)
        # if i wanted union I would use |=
    return tuple(result)

print(get_common_elements_unlimited("abc",['a','b'],('b','c')))

# let us try with more arguments
print(get_common_elements_unlimited("abc",['a','b'],('b','c'),{'b','a'},{'a','b','c'}))
# let us try with 2 strings
print(get_common_elements_unlimited("abba","abracadabra"))