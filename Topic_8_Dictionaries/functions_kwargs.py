# we can have a function that takes any number of keyword arguments
def print_kwargs(**kwargs):
    print("Start of keyword arguments")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(a=1, b=2, c=3)
print_kwargs(name="Valdis", age=25, city="Rīga")

# kwargs can be combined with regular arguments
def print_args_kwargs(*args, **kwargs):
    print("Start of arguments")
    for arg in args:
        print(arg)
    print("Start of keyword arguments")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_args_kwargs() # this is okay no arguments
print_args_kwargs(1, 2, 3, name="Valdis", age=25, city="Rīga")

# we can even add some default values
def print_args_kwargs(required_val,*args, debug=False, **kwargs):
    print("This value is required", required_val)
    print(f"Debug is {debug}")
    print("Start of arguments")
    for arg in args:
        print(arg)
    print("Start of keyword arguments")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_args_kwargs(42) # this is okay no extra arguments
print_args_kwargs(42,  1, 2, 3,debug=True, name="Valdis", age=25, city="Rīga")