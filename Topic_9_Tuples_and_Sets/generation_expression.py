# let's talk about generator expressions
# those are not tuple expressions although they seem like them - there are no tuple generators

# let's create a generator expression
# we will use generator expression to for squares of some numbers
squares = (x**2 for x in range(10)) # so looks like tuple version of list comprehension does it not?
print(squares)  # <generator object <genexpr> at 0x000001F9E5E4B200>
# so it is a generator object, in ways similar to range object, half-baked list or tuple
# we can iterate over it but not access elements by index
# we can always get tuples or lists out of them
square_list = list(squares)
print(square_list)
print(squares)  # [] - empty list as we have already consumed the generator
another_list = list(squares)
print(another_list)  # [] - empty list as we have already consumed the generator
# so we can only consume the generator once

# we can also use generator expressions in for loops
# let's print squares of numbers from 0 to 9
squares = (x**2 for x in range(10))
for square in squares: # so less memory consumption as we are not storing all the values
    print(square)

# of course for 10 values it does not matter but for 1000s of values it would

# similarly looping over reversed is more memory efficient than storing the reversed tuple
numbers = tuple(range(10))
for number in reversed(numbers): # faster than numbers[::-1]
    print(number)