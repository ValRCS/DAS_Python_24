# There is a long standing debate in the programming community about whether inheritance or composition is a better way to achieve code reuse.
# Inheritance is a mechanism where a new class is derived from an existing class. Inheritance allows us to reuse the code of an existing class and add new features to it.
# Composition is a mechanism where a class contains an object of another class. The contained object is responsible for the behavior of the containing class.
# More info: https://realpython.com/inheritance-composition-python/
# Wiki: https://en.wikipedia.org/wiki/Composition_over_inheritance

# let's create Auto from different classes

class Engine:
    def __init__(self, power, eng_type="Petrol"):
        self.power = power
        self.eng_type = eng_type
        print("Engine created!")
        self.display()

    def display(self):
        print("Power:", self.power)
        return self
    
class Wheel:
    def __init__(self, size, brand="Michelin"):
        self.size = size
        self.brand = brand
        print("Wheels created!")
        self.display()

    def display(self):
        print("Size:", self.size)
        print("Brand:", self.brand)
        return self
    
# let's add Seat class
class Seat:
    def __init__(self, material="Leather", color="Black"):
        self.material = material
        self.color = color
        print("Seat created!")
        self.display()

    def display(self):
        print("Material:", self.material)
        print("Color:", self.color)
        return self
    
class Auto:
    def __init__(self, 
                 maker, 
                 power, 
                 wheel_number=4, 
                 wheel_size=16, 
                 seats=5,
                 eng_type="Petrol",
                 tyre_brand="Michelin",
                 seat_material="Leather",
                 seat_color="Black"):
        print("Creating Auto...")
        self.maker = maker
        self.engine = Engine(power, eng_type=eng_type)
        # now we can store wheels in a list
        self.wheels = [Wheel(wheel_size, tyre_brand) for _ in range(wheel_number)] # list comprehension
        # for loop would be
        # self.wheels = []
        # for _ in range(wheel_number):
        #     self.wheels.append(Wheel(wheel_size))
        self.seats = [Seat(material=seat_material, color=seat_color) for _ in range(seats)]
        self.distance = 0
        print("Auto created!")
        self.display()

    def display(self):
        self.engine.display()
        for wheel in self.wheels:
            wheel.display()
        # we can call whatever methods we want here do not have to be display
        return self
    
    def drive(self, speed=60, duration=1):
        print(f"Driving at speed {speed} for {duration} hours")
        print(f"Total distance BEFORE: {self.distance}")
        self.distance += speed * duration
        print(f"Total distance AFTER: {self.distance}")
        return self
    
# let's create an instance of Auto
vw = Auto("VW", 100, 4, 17)
vw.drive(120, 0.2).drive(90,1.5)