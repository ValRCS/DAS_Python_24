# so input ALWAYS returns string
# name = "Valdis"
name = input("What is your name?")
print(f"Hello {name}!")
number = input("What is your favorite number?")
print(f"Nice I like {number} too")
# number is not a number yet
print(type(number)) # type just shows the data type of variable
# we need to cast it to actual number
number = float(number) # overwrite old value with numeric version
print(type(number))
int_number = int(number) # ja sagaidam ka lietotajs ievadis float
# tad vispirms parversham par float un tikai tad par int
print(int_number, type(int_number))