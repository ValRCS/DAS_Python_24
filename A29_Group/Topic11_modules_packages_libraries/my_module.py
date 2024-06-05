# why do we need modules in Python?
# 1. To break down large programs into small manageable and organized files.
# 2. To provide code reusability.
# 3. To implement namespaces. 
# On large projects, we could start running into name conflicts, so we can use modules to create namespaces.

# so what is a module in Python ?
# A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py appended.

# let's make a simple greeting function
def greet(name):
    print(f"Hello, {name}!")

# I could store some variables/constants
PI = 3.14159

# also we could store classes
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hello, {self.name}!"

# for modules to be used by others we do not want to run any code in the module
# print("Hey I am a module!")
# print(greet("Valdis"))
# print(PI)
# valdis = Person("Valdis")
# print(valdis.greeting())