# In Python we use comparison to compare two items/objects/values
# we have a special data type called Boolean that is the result of these comparison
is_spring = True # note capital True
is_snowing = False
print(is_spring, is_snowing)
# underneath True is represented by 1 and False by 0
# Booleans only HAVE two values, no MAYBE
print(type(is_spring))
print(type(is_snowing))

# one way to get Booleans is to use comparison
# usually one side or both will have variables
print("2*2 == 4", 2*2 == 4) # note == is not assignment it is comparison!
print(2*2 == 5)
# generally in Python we compare similar types
print(3.14 == 4) # is ok to compare
print(3.14 == "Valdis") # so this is okay but generally we want similar types
# greater
print("4 > 5", 4 > 5)
print("5 > 4", 5 > 4)
# lesser but let's use variables
a = 2
b = 4
print(f"{a} < {b} ? {a<b}")
print(f"{b} < {a} ? {b<a}")
# i might need boolean later then I can save it in a variable
is_a_less_b = a < b # the right side will be evaluated first
print(f"Aha so {a} < {b} is {is_a_less_b}")
# we also have less or equal and greater than equal
print("a*a >= b ?", a, b, a*a >= b)
print("a*a <= b ?", a, b, a*a <= b)
# in Python we can chain our comparisons
c = 100
print("a < b < 50 < c ?", a < b < 50 < c)
print("a < b < 500 < c ?", a < b < 500 < c)

# then we have inequality !=
print("is a not equal to 2?", a != 2) # False because a == 2 !!!
print("is a not equal to 9000?", a != 9000) # True because a is NOT 9000 !

# finally we have is operator
# is actually compares objects in memory
# so is returns True if we are comparing EXACT same objects
# this can be useful when checking for more complex object identities
# it can also be used to check if something is None

# we have special data type called None - represents nothing,nil, null in other languages
mr_nemo = None
print(f"Is mr_nemo actually None?", mr_nemo is None)


