# I could import my_module here as well
# import my_module # think of copy pasting the code from my_module.py here
# however I will show some other ways of importing

# first alternative is to use an alias
# popular aliases are two or three letter acronyms
# import my_module as mm # so different name
# # programmers are lazy so we want to type less
# # I can now use my greet function
# mm.greet("Rūta") #note I am using my_module. to access the function
# print(mm.PI) # I can access my constant
# valdis = mm.Person("Valdis") # I can use my class
# print(valdis.greeting()) # I can call my class method

# # i would this is my favorite way of importing

# there are a couple more ways of importing but they can lead to some problems
# I could import specific functions/classes/constants from the module
# from my_module import greet, PI, Person # here I imported all 3 but i could import just 1
# with this we lose the namespace so we can not use my_module. anymore
# i use these directly
# greet("Rūta") #note I am using my_module. to access the function
# print(PI) # I can access my constant
# valdis = Person("Valdis") # I can use my class

# the above approach would be useful if the module has a lot of functions and I only need a few

# if I have a name collission I could rename specific imports
# from my_module import greet as my_greet, PI as my_PI, Person as my_Person
# # again I could import just one or two functions/classes/constants
# # my opinion is that it would be better to just rename the module itself


# there is one way which is not recommended - AVOID
# from my_module import * # this will import everything from the module
# # this is bad because we do not know what we are importing
# we could overwrite some functions/constants/classes from our own module
