# static methods and attributes
# sometimes we want to have methods and attributes that belong to the class and not to the instance
# this means that we can call the method without creating an instance

# let's see an example
# let's say we have a class that represents mathematical operations

class Math:
    # let's add a static method that returns the value of pi
    @staticmethod
    def pi():
        return 3.14159265359

    # let's add a static method that returns the value of e
    @staticmethod
    def e():
        return 2.71828182846

    # let's add a static method that returns the value of golden ratio
    @staticmethod
    def golden_ratio():
        return 1.61803398875

    # let's make a method that returns area of a circle
    @staticmethod
    def circle_area(radius):
        return Math.pi() * radius**2
    
    # let's make a method that returns area of a square
    @staticmethod
    def square_area(side):
        return side**2
    

# let's call the static methods
print(Math.pi())
print(Math.e())
print(Math.golden_ratio())
print(Math.circle_area(10))
print(Math.square_area(5))

# so static methods are defined with @staticmethod decorator
# this is good for grouping related methods together
# we could create an instance of Math but no real need here
new_math = Math()
print(new_math.circle_area(10)) # would work but not needed
# new math object is not really needed could use Math directly

# there are also class methods that means we have access to the class itself but no need here

# to recap static methods are useful when we want to group related methods together

# in effect this is like using a blueprint to store a calculator on it