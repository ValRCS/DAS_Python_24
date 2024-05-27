# dictionaries can be used as keyword arguments
# so we can create a function that takes unlimited keyword arguments

def unlimited_kwargs(**kwargs):
    print(f"Starting with {len(kwargs)} keyword arguments")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# we can call this function with any number of keyword arguments
unlimited_kwargs(a=1, b=2, c=3)
unlimited_kwargs(name="John", age=30)
unlimited_kwargs()

# practical example
def create_person(**person_info): # so no need to call this argument kwargs, it can be anything
    person = {}
    for key, value in person_info.items():
        person[key] = value
    return person

person1 = create_person(name="Jānis", age=30, city="Riga")
print(person1)
person2 = create_person(name="Līga", age=25, city="Riga", country="Latvia")
print(person2)

# alternatively we could write a function that expects a dictionary
def create_person(person_info):
    person = {}
    for key, value in person_info.items():
        person[key] = value
    # above could be just a .copy() method so not much point
    return person