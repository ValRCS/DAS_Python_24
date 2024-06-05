import math

def sum_prod(*args):
    if len(args) == 0:
        return 0 # could return something else such as None or raise an exception
    # total_sum = sum(math.prod(arg) for arg in args)
    # print(total_sum)
    return sum(math.prod(arg) for arg in args) # we are using generator expression here
# generation expressions are similar to list comprehensions
# they are more memory efficient when we don't need to store the whole list