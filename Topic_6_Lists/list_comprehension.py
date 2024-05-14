# creating and filtering lists is very common
# so Python has a shortcut for that called list comprehension

# let's say we have a list of foods
foods = ['apple', 'banana', 'carrot', 'donut', 'egg', 'fries', 'grapes', 'hamburger', 'ice cream', 'jelly']
# we want to filter out only the foods that contain the letter 'a'
foods_with_a = []
for food in foods:
    if 'a' in food:
        foods_with_a.append(food)
print(foods_with_a)

# since this is so common Python has a shortcut for this
# we can use list comprehension
# [expression for item in iterable if condition]
also_foods_with_a = [food for food in foods if 'a' in food] # if is optional
# this is the same as the for loop above
print(also_foods_with_a)

# how about squaring numbers from 1 to 10
# normal way
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# list comprehension
also_squares = [i**2 for i in range(1, 11)]

name = "Valdis"
# let's create a two dimensional list of letters and their unicode values
name_unicode = [[letter, ord(letter)] for letter in name]
print(name_unicode)
# without list comprehension
also_name_unicode = []
for letter in name:
    also_name_unicode.append([letter, ord(letter)])
print(also_name_unicode)



# when to use list comprehension?
# when you want to create a new list from an existing list
# when you want to filter out some elements from a list
# when you want to transform elements of a list
# use full loops when you need to do more complex operations