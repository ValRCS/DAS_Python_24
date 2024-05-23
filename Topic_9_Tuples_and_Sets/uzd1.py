# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, 
# aritmētisko vidējo un lielāko vērtību no virknes.
# get_min_avg_max([0,10,1,9]) -> (0,5,10)
# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 
# def get_min_avg_max(sequence):
#     sequence = list(sequence)
#     sequence.sort() # could have used sequence = sorted(sequence)
#     # if I have a big sequence then sorting is a bit longer than min max and sum
#     # min, max and sum are O(n) operations, but sorting is O(n log n)
#     avg = round(sum(sequence)/len(sequence))
#     return sequence[0], avg, sequence[-1]

def get_min_avg_max(sequence):
    if not sequence:
        raise ValueError("The input sequence must not be empty.")
 
    min_val = min(sequence)
    max_val = max(sequence)
    avg_val = sum(sequence) / len(sequence)
 
    return min_val, avg_val, max_val
 
print(get_min_avg_max([0, 10, 1, 9]))  # Output: (0, 5.0, 10)

res = get_min_avg_max([0,10,1,9])
print(res)

def get_min_med_max(sequence):
    sequence = list(sequence)
    sequence.sort()
    my_min = sequence[0] # works on strings
    my_max = sequence[-1] # works on strings
    also_min = min(sequence) # does it work on strings
    print(my_min, also_min)
    l = len(sequence)
    if l%2 == 0:
        # try:
        #     med = (sequence[ round(l/2) -1 ] + sequence[ round(l/2) ]) / 2
        # except: # so this means that we have strings in the sequence
        #     med = sequence[ round(l/2) -1 ] + sequence[ round(l/2) ] 
        # similar but with if else
        if type(sequence[0]) == str:
            med = sequence[ round(l/2) -1 ] + sequence[ round(l/2) ]
        else:
            med = (sequence[ round(l/2) -1 ] + sequence[ round(l/2) ]) / 2
    else:
        med = sequence[ round(l/2) ]
    return sequence[0], med , sequence[-1]

print(get_min_med_max([0,10,1,9]))  # Output: (0, 5.0, 10)
print(get_min_med_max([0,10,1,9, 11]))  # Output: (0, 9, 11)
print(get_min_med_max("bbaac")) # Output: ('a', 'b', 'c')
# let's try with 6 letters
print(get_min_med_max("bbbaac")) # Output: ('a', 'bb', 'c')