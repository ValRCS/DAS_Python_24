# let's build some houses
# first I need to import House class
import house # I could also import House class directly from house.py module

# let's make a house
house1 = house.House("Rīga, Brīvibas 3", 100)
house1.print_address().print_area().print_floors().print_rooms()


# let's make a whole subdivision
# houses = [house.House(f"Mārupe, Rīgas iela {i}", 100) for i in range(1, 11, 2)]
# instead of above I could have used regular loop
houses = []
for i in range(1, 11, 2):
    houses.append(house.House(f"Mārupe, Rīgas iela {i}", 100))

# let's print all houses
for house in houses:
    house.print_address().print_area().print_floors().print_rooms()

# I could store my house objects in a list, dictionary, in SubDivision class etc etc

# without __str__ method print will be very uninformative
# let's print first house
print(house1) # this is without our own __str__ method
# we could find this info with id function so not very useful