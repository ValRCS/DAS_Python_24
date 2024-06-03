# we already saw __init__ method which is most common dunder method
# there are about 100 more dunder methods
# full list: https://docs.python.org/3/reference/datamodel.html#special-method-names

# let's create a class that uses some of the dunder methods
# let's make Salad class

class Salad:
    # __init__ method is called when object is created
    def __init__(self, name, ingredients:tuple=()):
        self.name = name
        self.ingredients = ingredients
        print("Salad created")
        # now I could print myself
        print(self)
    # __str__ method is called when object is printed
    def __str__(self):
        # only requirement is that we return string any string at all
        return f"Salad {self.name} with {', '.join(self.ingredients)}"
    # __len__ method is called when len function is called
    def __len__(self):
        return len(self.ingredients)
    
    # let's add __add__ method which lets us use + operator
    def __add__(self, other):
            # here we could add two salads together
            # we could add ingredients together
            # we could add names together
            # we could add salads together
            # we could add salads and strings together
            # we could add salads and integers together
            # we could add salads and lists together
            # we could add salads and dictionaries together
            # we could add salads and other objects together
            # we could add salads and None
            new_name = f"{self.name}___{other.name}"
            new_ingredients = self.ingredients + other.ingredients
            return Salad(new_name, new_ingredients)


thousand_island = Salad("Thousand Island", ("lettuce", "tomato", "cucumber", "onion", "thousand island dressing"))
# print(thousand_island)
# how long is salad?
print(f"Salad has {len(thousand_island)} ingredients")

# let's make another salad
caesar = Salad("Caesar", ("lettuce", "croutons", "parmesan", "caesar dressing"))

# franken salad
franken = thousand_island + caesar # so we've overloaded + operator
print(franken) # note that creation also used __str__ method so we got print twice

# basic idea is to use use sensive overloading symbols
# remember our set example from previous session <=, >=, ==, !=, <, > for set operations

# i would say only __init__ and __str__ should be used in most cases