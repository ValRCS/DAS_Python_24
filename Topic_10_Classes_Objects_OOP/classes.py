# Classes and Objects in Python
# Classes -> Blueprint for objects
# Objects -> Instance of a class - concrete realization of a class
# in Classes we describe what type of data we want to store and what operations we want to perform on that data
# Thus Classes provide a blueprint for data and methods that we want to use in our program
# Methods -> Functions that are associated with a class

# one reason to learn about classes and object in Python is that Python is an object-oriented programming language
# almost everything in Python is an object, with its properties and methods
print(type(5)) # <class 'int'>
# so here we see that 5 is a object of class int
# so this means that Python somewhere has a blueprint for the int class

# let's see how would we live without classes and objects to create multiple garages
# so we want to build a garage cooperative where people can rent a garage to store their cars

# we could use a list of dictionaries to store the data about each garage
garage1 = {'owner': 'Jānis', 'cars': ['BMW', 'Mercedes'], "empty_paint_cans":5}
garage2 = {'owner': 'Pēteris', 'cars': ['Audi', 'VW'], "empty_paint_cans":3}
garage_list = [garage1, garage2] # so we can store data about multiple garages in a list
# now we would like to see all the cars in one garage
# we would have to write a function to do that
def show_cars(garage):
    for car in garage['cars']:
        print(car)

show_cars(garage1)
# so this works but function is separate from the data and we have to pass the data to the function
# if our data grows and we have more functions that work with the data, we have to pass the data to

# inevitably we will have a hard time to find the function that we need to work with the data
# especially if we have not worked on this code for a while or maybe it is someone else's code

# classes and objects we create from them allow us to easily group data and functions that work with that data
# then we have a clear structure and we can easily find the functions that work with the data

# let's start with a completely empty class
class EmptyClass:
    pass # pass is a keyword in Python that does nothing, we needed to do something in the class

# essentially we have a blank blueprint for an object

empty_object = EmptyClass() # we create an object from the class
# now we can attach data to the object
empty_object.data = 5
# now we can access the data from the object
print(empty_object.data) # 5
# we could attach a garage 
empty_object.garage = garage1
print(empty_object.garage) # {'owner': 'Jānis', 'cars': ['BMW', 'Mercedes'], 'empty_paint_cans': 5}
# so we gain some convenience from blank class - blueprint for an object
# however it is much nicer if we define the class with some data and functions that work with that data

# let's make a class SimpleHouse
class SimpleHouse:
    rooms = 5
    def show_rooms(self): # self refers to particular object that we are working with NOT class!
        # here we could add some validation, verification, etc.
        print(self.rooms)
    def increase_room_size(self, rooms_to_add=1, verbose=False):
        self.rooms += rooms_to_add
        if verbose:
            print(f"Added {rooms_to_add} rooms to the house")
            print(f"Now we have {self.rooms} rooms")

# above is a simple blueprint for a house
# now we can make unlimited number of houses from this blueprint
house1 = SimpleHouse()
# now we can print its rooms
house1.show_rooms() # 5
# we can also change the number of rooms in the house
house1.rooms = 6
house1.show_rooms() # 6
# we can add 5 more
house1.rooms += 10
house1.show_rooms() # 16
# now we can create another house
house2 = SimpleHouse()
house2.show_rooms() # 5
# note that number of rooms in house2 is still 5 because we have not changed it
house2.increase_room_size(3, verbose=True)


# so when we call SimpleHouse() each time we create a new object with its own data - there are some exceptions
# we can still attach arbitrary data to the object
house1.garage = garage1 # we can attach a garage to the house it is possible but bad practice

# main idea behind OOP is that we stick to this structure of class blueprints and then objects from them

# our SimpleHouse class is not very useful because we can only store the number of rooms
# also each time we create a new house it has 5 rooms, how about starting with 4 rooms?
# it would be nice not to wait for the house to be built to add rooms

# let's make a class House
class House:
    # __init__ is called just after the object is created, it is not technically constructor but very similar
    def __init__(self, name="", address="", rooms=4): # __init__ is a special method that is called when we create a new object
        self.name = name # self.name and name do not have to match but it is generally a good idea to match them
        self.address = address # in reality address could have been an object of type Adress
        self.rooms = rooms
        # so here concrete object already has two properties name and rooms
        # now we can call our methods on the object from any other method
        self.print_address() # so each new house will also print its address

    def show_rooms(self):
        print(self.rooms)
    def increase_room_size(self, rooms_to_add=1, verbose=False):
        self.rooms += rooms_to_add
        if verbose:
            print(f"Added {rooms_to_add} rooms to the house")
            print(f"Now we have {self.rooms} rooms")
    def print_address(self):
        # here we could add extra formatting, etc.
        # here we could add extra if check if no name or address is given
        if self.address:
            print(f"Address of house called {self.name} is {self.address}")

# now we can really create a house with 4 rooms
real_house = House() # default is 4 rooms
bigger_house = House(rooms=10) # we can also create a house with 10 rooms
real_house.show_rooms() # 4
bigger_house.show_rooms() # 10
house_with_name = House(name="Birzmaļi", address="Jūras 23", rooms=6) # neither name nor rooms are default
print("Mana māja ir", house_with_name.name) # Birzmaļi
# address is not printed because we have not defined a method to print it
# we could add a method to print the address
house_with_name.print_address() # Jūras 23

# now let's make even bigger blueprint for a house
# we will call it ModernHouse
class ModernHouse():
    # again __init__ is called just after the object is created
    def __init__(self, name="", address="", rooms=4, floors=1):
        self.name = name
        self.address = address
        self.rooms = rooms
        self.floors = floors
        # self.print_address() # no need for this if I can now print
        print(self) # this will print the object (not very useful but possible
    # there are many __dunder__ methods in Python, __init__ is just one of them
    # full list is here: https://docs.python.org/3/reference/datamodel.html#special-method-names
    # one very useful is __str__ that is called when we try to print the object
    def __str__(self):
        # only requirement is that we are returning a string
        # we could prepare the string here main thing that we DO NOT PRINT IT! just return
        return f"ModernHouse object called {self.name} with {self.rooms} rooms and {self.floors} floors"
    
    # i can make my own + for the object using __add__ method
    def __add__(self, other):
        rooms = self.rooms + other.rooms
        floors = self.floors + other.floors
        name = f"{self.name} and {other.name}"
        # we will return a new object of the same class
        return ModernHouse(name=name, rooms=rooms, floors=floors)
    # we can define our own -, *, /, <, >, ==, !=, etc. methods 

    # my own methods - any name without __ is fine, just remember self in method definition
    def show_rooms(self):
        print(self.rooms)
        # if we do not need to return anything it is a good idea to return self
        return self
    def increase_room_size(self, rooms_to_add=1, verbose=False):
        self.rooms += rooms_to_add
        if verbose:
            print(f"Added {rooms_to_add} rooms to the house")
            print(f"Now we have {self.rooms} rooms")
        return self
    def print_address(self):
        if self.address:
            print(f"Address of house called {self.name} is {self.address}")
        return self
    def show_floors(self):
        print(self.floors)
        return self
    def increase_floors(self, floors_to_add=1, verbose=False):
        self.floors += floors_to_add
        if verbose:
            print(f"Added {floors_to_add} floors to the house")
            print(f"Now we have {self.floors} floors")
        return self
    
# now that we are returning object itself we can CHAIN methods

modern_house = ModernHouse(name="Homer's", address="Springfield", rooms=6, floors=2)
# now we can chain methods like this
modern_house.show_rooms().increase_room_size(3, verbose=True).show_rooms().increase_floors(1, verbose=True).show_floors()
# of course we could have written this line by line
modern_house.show_rooms()
modern_house.increase_room_size(5, verbose=True)
modern_house.show_rooms() # 14
# now if I print the object I get a memory address - not very useful
print(house1) # <__main__.SimpleHouse object at 0x7f8b1c7b3d30>
print(modern_house) # ModernHouse object called Homer's with 14 rooms and 3 floors

# let's make millhouse's house
millhouse_house = ModernHouse(name="Millhouse's", address="Evergreen Terrace", rooms=3, floors=1)
# we can check the types
print(type(millhouse_house)) # <class '__main__.ModernHouse'>

# so to summarize this first section
# we create a class with a blueprint for an object
# we instantiate an object from the class using the class name
# we can attach data to the object using self
# we use __init__ to set the initial data of the object
# we can attach functions to the object that work with the data
# we can chain the methods if we return self from the methods
# we have multiple __dunder__ methods that we can use to customize the behavior of the object

# again I can make as many houses I want and store them in a list
# let's make a development of houses in Oak street
# oak_street_houses = []
# for i in range(5):
#     oak_street_houses.append(ModernHouse(name=f"House No. {i+1}", address=f"Oak street {i+1}", floors=2))

# # now I can createa a frankenhouse with add
# frankenhouse = modern_house + millhouse_house
# # + creates a new object thus print is called from __init__ in new object
# print(frankenhouse) # ModernHouse object called Homer's and Millhouse's with 17 rooms and 4 floors

def create_houses(n)->list[ModernHouse]:
    houses = []
    for i in range(n):
        houses.append(ModernHouse(name=f"House No. {i+1}", address=f"Oak street {i+1}", floors=2))
    return houses

oak_street_houses = create_houses(5)
# now with type hints I can see that oak_street_houses is a list of ModernHouse objects