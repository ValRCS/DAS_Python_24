# information hiding is the principle of hiding the internal state and implementation details of an object
# and only exposing the necessary parts to the outside world.

# typically it is done through private attributes and methods

# in python we can use single underscore _ to indicate that an attribute or method is private

# double underscore __ is used to make an attribute or method strongly private

# Python is quite liberal with this and does not enforce it

# let's see an example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._address = "Rīga"
        self.__phone = "12345678"

    # let's add a method to display the phone number
    def display_phone(self):
        print("Phone:", self.__phone)

    # let's add a method to change the phone number
    def change_phone(self, phone):
        self.__phone = phone

    # let's add a method to display the address
    def display_address(self):
        print("Address:", self._address)

    # let's add a method to change the address
    def change_address(self, address):
        self._address = address

# let's create an instance of Person
alice = Person("Alice", 25)
bob = Person("Bob", 30)

# let's try to access the phone number
try:
    print(alice.__phone)
except AttributeError:
    print("AttributeError: 'Person' object has no attribute '__phone'")

# there is a way to access it but it is not recommended
# it would be _Person__phone
print(alice._Person__phone) # so not really private

# let's try to change the phone number
alice.change_phone("87654321")
alice.display_phone()

# now city is accessible in any way
print(alice._address) # single _ is just a convention
alice.display_address()

# so takeway is that we use _ to indicate that an attribute or method is private
# we use __ to indicate that an attribute or method is strongly private