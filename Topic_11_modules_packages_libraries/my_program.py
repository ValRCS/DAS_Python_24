# often when we write a program we want to use an external library
# or possibly a module that we have written ourselves
# it could be a package or a module

# modules are just python files that contain functions, classes and variables
# how do we create a module?
# we just create a python file and write some code in it

# why should we create modules?
# to organize our code
# to reuse our code
# to avoid naming conflicts - if we have a function with the same name in two different modules
# we can use the module name to access the function

# now I can import my_module and use the greeting function
import my_module

print(my_module.greeting("Valdis"))

# i can use my_module.PI
print(f"Value of PI is {my_module.PI}")

new_person = my_module.Person("Valdis", 40)
print(new_person.greet())

another_person = my_module.Person("Līga", 35)
print(another_person.greet())

# we have some other ways of importing
# very common is to provide an alias for the module
# partially it is motivated by laziness
# if the module name is long we can provide a shorter alias
# a good programmer is a lazy programmer
# import my_module as mm  # again typical to see 2 or 3 letter alias

# print(mm.greeting("Valdis"))
# print(f"My PI is {mm.PI}")

# # disclaimer I like the above aliasing but some people do not like it

# there is a third way to import functions, classes and variables on a need to use basis

# from my_module import greeting, PI, Person # so add is not imported

# print(greeting("Valdis"))
# print(f"My PI is {PI}")
# new_person = Person("Valdis", 40)

# potentially this can create a naming conflict
# what if we already created another PI variable in our program?
# same would go for Person class or greeting function

# we can import these functions, classes and variables with an alias as well
# from my_module import greeting as gr, PI as pi, Person as PRS # make up your own alias

# print(gr("Valdis"))
# print(f"My PI is {pi}")
# new_person = PRS("Valdis", 40)

# above is also a bit dangerous because again we could have some naming conflicts

# that is why my advice is to use first way of importing just whole module
# alternatively you could use the second way of importing with alias

# there is also the fifth way of importing everything from a module
# from my_module import * # this is generally not recommended, AVOID THIS
# why? because you do not know what you are importing
# in a large library you could be importing hundreds of functions, classes and variables
# creating a big mess and multiple naming conflicts