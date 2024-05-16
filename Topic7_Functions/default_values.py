# often it can be beneficial to provide default values for function arguments

# let's say I want to print a greeting to a person
# I could write a function like this
def greet_person(name, greeting):
    print(f"{greeting}, {name}")

# however I would like to have a default greeting
def greet_person_with_default(name="Valdis", greeting="Hello"):
    print(f"{greeting}, {name}")

# now I can use the function without the second parameter
greet_person_with_default() # both parameters are default
greet_person_with_default("Rūta")
# but I can also provide a custom greeting
greet_person_with_default("Valdis", "Sveiki")

# Main idea is to use "Sane" defaults
# defaults that will work in most cases
# defaults that are most common

# for example print function has a default end="\n" which is a newline character

# i can also supply name of parameters when calling the function
greet_person_with_default(greeting="Labdien", name="Līga") # note I switched the order
# generally it is better to use correct order of parameters
# but named parameters can be useful when you have many parameters and you want to make it clear what you are passing
# for example for print I could printing multiple values with a separator and also I want custom end
print("Valdis", "Līga", "Rūta", "Liene", sep="), (", end="!\n")
# better to use f-strings for this but just to show the example

# i can call greeting with only one parameter
greet_person_with_default("Līga", greeting="")
greet_person_with_default(66, greeting=900) # works because we are using f-strings inside and nothing else