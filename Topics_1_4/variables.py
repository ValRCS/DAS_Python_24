# variables
# we need to store data when we do work in program
# in Python we declare variables when we first declare
# unlike other languages we do not say anything else
# = is used for assignment it is NOT equality!!
name = "Valdis" # so I store "Valdis" in name (technically I point to string)
university = "RTU"
message = name + " teaches at " + university
print(message)
print("My first name is", name) # i can use , for space by default
# this is so called f-string, or string template
big_message = f"My name is {name} and I work at {university}"
print(big_message)
a = 2
b = 5
result = b * a
print(f"{a} times {b} equals {result}")
# typically in a normal program all data in memory would be lost
# when we finish running
# in Thonny the program is still alive

not_formatted = "My name is {name}" # without f {} are just symbols
formatted_text = f"My name is {name}"
print(not_formatted)
print(formatted_text)
# variables automatically (dynamically) determine what data type they should be
print("name") # just text not variable!!
print(name) # whatever is variable name pointing to
print(name, type(name)) # I can check what data type is variable
print(a, type(a)) # integer data type
float_data = b / a # so float_data will hold b divided by a
print(float_data, "is of type", type(float_data))
# not saved yet
