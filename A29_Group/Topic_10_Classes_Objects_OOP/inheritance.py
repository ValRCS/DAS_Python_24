# there is also a way to inherit from other classes
# idea is that we have a class that already does most of the things we want
# we can inherit from that class and add some new functionality

# let's start with Animal class for base

class Animal:
    def __init__(self, name, age, kind="unknown"):
        self.name = name
        self.age = age
        self.kind = kind
        print(f"Animal {name} created")
    def make_sound(self):
        print("Some sound")
        return self
    
# let's make a mouse from this class
mouse = Animal("Jerry", 1, "mouse")
mouse.make_sound()

# instead we could make a class for a dog

class Dog(Animal): # here Dog class inherits ALL from Animal class!
    # i already have an __init__ method in Animal class so I could skip that if I wanted
    # but let's do it anyway
    def __init__(self, name, age, breed, kind="dog"):
        super().__init__(name, age, kind) # here I call __init__ method of parent class Animal
        # I could have set the name, age, kind by hand here without super().__init__ call
        self.breed = breed
        print(f"Dog {name} created")

    # let's make a bark method
    def bark(self, custom_bark = "Woof Woof"):
        print(f"{self.name} is barking - {custom_bark}")
        return self
    
# let's make a dog
dog = Dog("Rex", 2, "bulldog")
dog.make_sound()
dog.bark()

# this looks great on paper but in practice it is more common to use composition
# there is lively debate on this topic
# https://en.wikipedia.org/wiki/Composition_over_inheritance
# https://realpython.com/inheritance-composition-python/