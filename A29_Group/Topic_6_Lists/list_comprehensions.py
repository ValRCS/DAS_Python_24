# when working with lists we commonly need to either filter some values or transform them in some way
# list comprehensions are a concise way to do this

# Example 1: filtering values

numbers = list(range(10)) # again range is not a list but we can apply the list function to it
print(numbers)
# let's say we want to filter odd numbers
# with loop we can do this
odd_numbers = [] # start with empty list
for number in numbers: # so typical singular noun for the variable representing each element
    if number % 2 == 1: # if the number is odd
        odd_numbers.append(number)
print(odd_numbers)

# so list comprehensions are a concise way to do this
# syntax is [expression for item in iterable if condition]
also_odd_numbers = [number for number in numbers if number % 2 == 1]
# number could be any name, it's just a variable name could be n or x or whatever
# numbers has to be iterable, could be string, list, tuple, set, dictionary and others

# similarly I would like to create squares of all numbers
# without list comprehension
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

# with list comprehension
also_squares = [number ** 2 for number in numbers] # note no need for if condition it is optional
print(also_squares)

# we can combine both filtering and transforming
# so let's say we want to filter even numbers and then square them
# with loop
even_squares = []
for number in numbers:
    if number % 2 == 0:
        even_squares.append(number ** 2)
print(even_squares)

# with list comprehension
also_even_squares = [number ** 2 for number in numbers if number % 2 == 0]
print(also_even_squares)

# so when should you use list comprehensions?
# when the logic is simple and can be expressed in a single line
# list comprehensions are slightly faster than loops but not significantly

# we do not have to use list as something we iterate over
# we could use a string for example
name = "Valdis"
letters = [letter for letter in name]
print(letters)
# for this example actually even simpler would be
also_letters = list(name) # so you pass iterable to list function
print(also_letters)

# we can use list comprehensions to build more complex data structures
# for now let's create a list of lists where first item is the number and second item is the square of that number
number_squares = [[number, number ** 2] for number in numbers]
print(number_squares)

# if we did not use list comprehension we would have to do this
also_number_squares = []
for number in numbers:
    also_number_squares.append([number, number ** 2]) # if we used extend it would flatten the list
print(also_number_squares)

# how do we access elements in a list of lists?
# we can use two indexes
# let's get 6th element
print(number_squares[5]) # remember 0 based indexing
# so last item in the 6th element
print(number_squares[5][1]) # so 2nd element in the 6th element
print(number_squares[5][-1]) # we can use negative indexes to count from the end

# More on List Comprehensions
# Official Docs: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# Unofficial Docs: https://realpython.com/list-comprehension-python/