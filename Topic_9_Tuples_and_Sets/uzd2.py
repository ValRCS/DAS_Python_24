# 2. Kopējie Elementi
# Uzrakstiet funkciju,kas atgriež tuple ar kopējiem elementiem trijās virknēs. Virknes var būt list,tuple,string.
# get_common_elements(seq1,seq2,seq3)
# get_common_elements("abc",['a','b'],('b','c')) -> ('b',) # tuple are vienu element šim elementam seko komats
# # atceramies, ka mēs varam pārveidot virknes uz set ar set(virkne), un set uz tuple ar tuple(myset)
# PS Tiem, kas nav pirmo reizi ar pīpi uz jumta, padomāsim, vai varam uztaisīt funkciju, kas spēj apstrādat patvalīgu skaitu virkņu

def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    # common_elements = set1.intersection(seq2, seq3) # works with any sequence type
    common_elements = set1 & set2 & set3 # for this we need sets1,2,3 to be sets
    return tuple(common_elements)

print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))  # Output: ('b',)

def get_common_elements_any(*sequences, is_sorted=False):
    if not sequences:
        # raise ValueError("At least one sequence is required.")
        return tuple() # so we return empty tuple
 
    common_elements = set(sequences[0]) # careful not to start with empty set here
 
    # Iterate through the rest of the sequences and find the intersection
    for seq in sequences[1:]:
        common_elements &= set(seq) # same as common_elements = common_elements.intersection(set(seq))
 
    if is_sorted:
        common_elements = sorted(common_elements) # here we change set to list

    return tuple(common_elements)
 
print(get_common_elements_any("abc", ['a', 'b'], ('b', 'c')))  # Output: ('b',)
print(get_common_elements_any("abc", "abcd", "abcf"))  # Output: ('a', 'b', 'c')
print(get_common_elements_any("abc", "abcd", "abcf", is_sorted=True))  # Output: ('a', 'b', 'c')
print(get_common_elements_any([1, 2, 3], (2, 3, 4), [2, 5], (2,2,5,6,17,299)))  # Output: (2,)