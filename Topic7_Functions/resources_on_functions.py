# let's make a list of urls to learn more about functions

function_resources = [

# official Python docs
    "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
    "https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions",
    "https://docs.python.org/3/tutorial/controlflow.html#default-argument-values",
    "https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments",
    "https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists",
    "https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists",
    "https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions",
    "https://docs.python.org/3/tutorial/controlflow.html#documentation-strings",
    "https://docs.python.org/3/tutorial/controlflow.html#function-annotations",
    # realpython
    "https://realpython.com/defining-your-own-python-function/",
    "https://realpython.com/python-kwargs-and-args/",
    "https://realpython.com/python-return-statement/",
    # w3schools
    "https://www.w3schools.com/python/python_functions.asp",
    # google's python class
    "https://developers.google.com/edu/python/introduction#user-defined-functions",
]

# let's print out the urls
# but a first a function to do that
def print_resources(resources: list[str]):
    for resource in resources:
        print(resource)

print_resources(function_resources)