# 1. Min, Avg, Max
 
 
 
def get_min_avg_max(sequence):
       min_value = min(sequence)
       max_value = max(sequence)
       avg_value = round(sum(sequence)/len(sequence))
 
       return min_value, avg_value, max_value
 
result = get_min_avg_max([0, 10, 1, 9])
print(result)

def get_min_med_max(sequence, verbose=False):
    min_value = min(sequence) # potential error here if bad data
    max_value = max(sequence)
    sorted_sequence = sorted(sequence) # potential error here if bad data
    # for strings sorted uses lexicographical order - alphabetical
    if verbose:
        print(sorted_sequence)
    n = len(sequence)
    mid = n // 2
    if n % 2 == 0:
        # check if elements are numbers
        if isinstance(sorted_sequence[mid - 1], (int, float)) and isinstance(sorted_sequence[mid], (int, float)):
            median_value = (sorted_sequence[mid - 1] + sorted_sequence[mid]) / 2
        else:
            median_value = (sorted_sequence[mid - 1] + sorted_sequence[mid])
    else:
        # for odd we do not care about the type
        median_value = sorted_sequence[mid]
    return (min_value, median_value, max_value )

result = get_min_med_max([0, 10, 1, 8])
print(result)
another_result = get_min_med_max([0, 10, 1, 9, 3])
print(another_result)

# let us try with some strings as well
result = get_min_med_max(['a', 'd', 'c', 'b'])
print(result)
another_result = get_min_med_max("Valdis")
print(another_result) # V is lowest, d is highest, a is median
print("Unicode of V", ord("V"))
print("Unicode of s", ord("s"))