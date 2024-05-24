# let's make a simple class Animal
# file name could be anything but for single class you should use the class name

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        print("Animal created!")
        self.display()

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Species:", self.species)
        return self
    
# let's add Dog as well inheriting from Animal
class Dog(Animal):
    def __init__(self, name, age, species="dog", breed="Mongrel"):
        self.breed = breed
        super().__init__(name, age, species)
        self.display()

    def bark(self, sound="Woof!"):
        print(sound)
    
# we have defined a class but we are not going to use it here
# instead we will import it in another file and use it there
    
# # let's create an instance of Animal
# winnie = Animal("Winnie", 2, "cat")
# darcy = Animal("Darcy", 2.5, "cat")