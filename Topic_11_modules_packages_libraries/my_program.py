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