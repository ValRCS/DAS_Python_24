# Now I would like to use my module from this file
# in Python I simply import the module
import my_module # think of copy pasting the code from my_module.py here
# now I get access to everything in the module
# 99% of time we do not want module to do anything 
# just import and use its functions/classes

# I can now use my greet function
my_module.greet("Rūta") #note I am using my_module. to access the function
print(my_module.PI) # I can access my constant
valdis = my_module.Person("Valdis") # I can use my class
print(valdis.greeting()) # I can call my class method
liga = my_module.Person("Līga")
print(liga.greeting())