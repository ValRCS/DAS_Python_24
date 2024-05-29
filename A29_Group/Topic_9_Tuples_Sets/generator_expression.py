# if there is list comprehension and dictionary comprehension
# how about tuple comprehension?
#
# instead we have generator expression
# generator expression is similar to list comprehension
# except we have () instead of []
# we get not a tuple but something that can be iterated over
# a bit similar to range() function
# let's see an example

# we can create a generator expression
gen = (x**2 for x in range(10))
print(gen) # not very useful just some generator object memory address
# i can always create a list from generator
gen_list = list(gen)
print(gen_list)

# interestingy gen is exhausted after we create a list from it
print(gen)
another_list = list(gen)
print(another_list) # so we get an empty list

# the idea behind generator expression is to be lazy
# we only give data when asked
# typically it is used to optimize memory usage
# if we only need to iterate over data once
# we can use generator expression
# also generator expressions can be used as function arguments

# example of looping over generator expression
gen = (x**2 for x in range(10)) # we needed to recreate generator
for item in gen: # gen is not a list it is a generator!
    print(item)

# more on generator expressions
# https://docs.python.org/3/tutorial/classes.html#generator-expressions
