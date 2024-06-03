# let's make a simple House class

# file name is not required to be the same as class name
# so here house.py could be named differently

class House:
    def __init__(self, address, area, floors=1, rooms=1):
        self.address = address
        self.area = area
        self.floors = floors
        self.rooms = rooms
        print(f"House at {address} created")
    def print_address(self):
        """Prints address of the house"""
        print(self.address)
        return self
    def print_area(self):
        print(self.area)
        return self
    def print_floors(self):
        print(self.floors)
        return self
    def print_rooms(self):
        print(self.rooms)
        return self
    
# I will not make house here, I will make it from different file

# I could make more class examples here
# I could have LuxuryHouse, Apartment, SubDivision classes etc etc