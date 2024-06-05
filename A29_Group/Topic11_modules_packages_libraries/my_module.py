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

# often we do want to run our module for testing purposes or just standalone

# Python offers such a feature called __name__ which is a built-in variable.
# we will use so called main guard
# idea run code only if this is the main file

if __name__ == "__main__":
    print("Hey I am a module!")
    print(greet("Valdis"))
    print(PI)
    valdis = Person("Valdis")
    print(valdis.greeting())
    # it is typical to run some tests in the module
    # i could use assert to perform some tests
    # assert is a keyword in Python that is used to check if a given logical expression is True or False.
    # if the expression is True, it will return None.
    # However, if the expression is False, it will raise an AssertionError exception.
    assert greet("Valdis") == None
    assert PI == 3.14159
    assert valdis.greeting() == "Hello, Valdis!"
# I could put an else here but it is not necessary
# we rarely want to run anything when importing a module