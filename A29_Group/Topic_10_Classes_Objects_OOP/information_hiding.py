# information hiding is the principle of hiding the internal state and requiring all interaction to be performed through an object's methods

# let's make a person whose address will be semi -hidden
# and phone number will be hidden

class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self._address = address # _ means that this is a semi-hidden attribute
        self.__phone = phone # here __ means that this is a hidden attribute, mangling
        print(f"Person {name} created")
    def print_address(self):
        print(self._address)
        return self
    def print_phone(self):
        # here we could check if we are authorized to print the phone number
        print(self.__phone)
        return self
    # then all manipulation with phone number should be done through methods
    # here is a classically named setter method
    def set_phone(self, phone):
        # here we could validate the phone number
        # is it 8 digits long?
        # is it only numbers?
        # and so on
        self.__phone = phone
        return self
    # also there is typically a getter method
    def get_phone(self):
        # again we could check if we are authorized to get the phone number
        return self.__phone
    
# let's make a person
person = Person("Ansis", "Rīga", "12345678")
# let's print address
person.print_address()
# we could print directly...
print(person._address)
# now how about phone?
person.print_phone()
# how about directly
try:
    print(person.__phone)
except AttributeError as e:
    print(e)
# in reality you could still access the hidden attribute

# let's try to change the phone number
person.set_phone("96785678")
person.print_phone()
# get phone
print(person.get_phone())