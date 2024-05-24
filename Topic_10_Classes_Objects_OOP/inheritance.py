# Concept of inheritance in Python
# idea is that we create a class that inherits attributes and methods from another class
# let's start with a simple example
# Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created!")
        self.display()

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        # i would have made this __str__
        return self # not needed but we can chain it later
    
janis = Person("Janis Joplin", 27)

# let's create a Musician class that inherits from Person
# idea is that we do not have to write the same code again
# we could have just created a Musician class from scratch but we want to show inheritance

class Musician(Person): # so here Musician has same blueprint as Person
    # I do not need to write __init__ method unless I want to add more attributes
    # let's add method
    def play_instrument(self, instrument): # note instrument is passed as argument not from inside
        print(f"Playing instrument {instrument}")

# let's create an instance of Musician
jimi = Musician("Jimi Hendrix", 27)
jimi.play_instrument("Guitar")

# in python we can actually inherit from multiple classes
# but it is not recommended as it can lead to confusion

# good uses of inheritance in practice
# let's say you have a nice web scraping class
# and you need to add some functionality to it

# similar for some database access class
# and you need to add some functionality to it

# so let's make a FullMusician class that inherits from Musician but also adds attributes and methods

class FullMusician(Musician): # so Musician already inherits from Person
    # i want to store the instrument in instance
    # so I will overwrite __init__ method that I got from Musician who got it from Person
    def __init__(self, name, age, instrument):
        self.instrument = instrument
        super().__init__(name, age) # calling parent class constructor
        self.display() # calling parent class method

    def play_my_instrument(self): # note instrument is not passed as argument
        print(f"Playing instrument {self.instrument}")

# let's create an instance of FullMusician
# so FullMusician inherits from Musician who inherits from Person
kurt = FullMusician("Kurt Cobain", 27, "Guitar")
kurt.play_my_instrument()
kurt.play_instrument("Harmonica") # this is from Musician class
