# so my_module is simply a python file that contains functions, classes and variables

# print("This will be printed when my_module.py is imported")
# generally we do not WANT our modules to DO anything when imported
# we want our modules to define functions, classes and variables
# Not to run code

# for example
def greeting(name):
    """This function greets the user"""	
    return f"Hello, {name}"

def add(a, b):
    """This function adds two numbers"""	
    return a + b

# i could store constants in a module
PI = 3.14159265

# i could store classes in a module

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} created")

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"


# we have an option to place so called main guard in our module
# this way we can run some code only when the module is run as a program
# and not when it is imported

# could make a main function and call it here
def main(): # main is just a convention could be any name
    print("This will be printed only when my_module.py is run as a program")
    print(greeting("Valdis"))
    print(add(5, 7))
    print(PI)
    new_person = Person("Valdis", 40)
    print(new_person.greet())
    another_person = Person("Līga", 35)
    print(another_person.greet())

# the next if statement has to be exactly like this
if __name__ == "__main__":
    # we could have a config function here
    main() 
    # we could have a cleanup function here

# when to use main guard?
# when you want to write some tests for your module
# second reason is when you want to run some code only when the module is run as a program
# and not when it is imported
# so you write a .py file that would run as a program
# but you also can import it and use its functions, classes and variables