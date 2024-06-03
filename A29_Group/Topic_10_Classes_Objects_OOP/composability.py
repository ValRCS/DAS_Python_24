# composability is the ability to combine simple objects or data types to build more complex ones

# let's make a car class
# car will consist of 4 wheels, 1 engine, 1 body

class Wheel:
    def __init__(self, diameter, brand="Michelin"):
        print(f"Wheel with diameter {diameter} and brand {brand} created")
        self.diameter = diameter
        self.brand = brand

    # spin wheel method
    def spin(self):
        # here you could actual spin the wheel
        print("Wheel spinning")
        return self

class Engine:
    def __init__(self, power, fuel="petrol", cylinders=4):
        self.power = power
        self.fuel = fuel
        self.cylinders = cylinders
        self.is_running = False
        print(f"Engine with power {power} and fuel {fuel} created with {cylinders} cylinders")
    # let's create a turn on engine method
    def turn_on(self):
        # here you could actual turn on the engine
        self.is_running = True
        print("Engine turned on")
        return self

class Body:
    def __init__(self, color="black", doors=4):
        self.color = color
        self.doors = doors
        print(f"Body with color {color} and {doors} doors created")
    # let's create body_check method
    def body_check(self):
        # here you could actual call to body sensors to check if everything is fine
        print("Body check done")
        return self

class Car: 
    def __init__(self, wheels:list[Wheel], engine:Engine, body:Body, maker="Toyota", make="Corolla", kilometers=0):
        self.wheels = wheels
        self.engine = engine
        self.body = body
        self.maker = maker
        # kilometers driver
        self.kilometers = kilometers
        print(f"Model {make} by {maker} created")
        print(f"This car has {len(wheels)} wheels, {engine.power} power, {body.color} color")
        # it has km kilometers driven
        self.show_kilometers()

    # show kilometers method
    def show_kilometers(self):
        print(f"This car has driven {self.kilometers} kilometers")
        return self

    # now let's creat a method to drive a car
    def drive(self, km=10):
        # here you could actual drive the car
        # here you could check if engine is on
        if not self.engine.is_running:
            print("Engine is not running")
            return self
        print("Car is driving")
        # spin all wheels
        for wheel in self.wheels:
            wheel.spin()
        # add kilometers
        self.kilometers += km
        return self

# let's create a car
# first we need to create wheels
# let's create 4 wheels with loop
wheels = [Wheel(17, "Pirelli") for _ in range(4)] # _ signifies that we do not care about the value

# let's create an engine
engine = Engine(200, "diesel", 6)

# let's create a body
body = Body("red", 2)

# let's create a car
car = Car(wheels, engine, body, "BMW", "M3")
car.body.body_check()
car.engine.turn_on()
car.show_kilometers().drive(67).show_kilometers().drive(100).show_kilometers()

vw = Car([Wheel(16), Wheel(16), Wheel(16), Wheel(16)], 
         Engine(150), 
         Body("blue", 4), 
         "VW", 
         "Golf", 
         kilometers = 197000)
vw.drive(50).show_kilometers().engine.turn_on() # engine turn_on returns engine not car!!
# note that above example showed that drive has internal logic that checks for running engine
# thus we did not actually drive the car because the engine was off :)
vw.drive(100).show_kilometers()   

