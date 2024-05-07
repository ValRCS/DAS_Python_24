# we might to ensure that user inputs a valid integer(or float)
# we can combine try except with while loop

# try block let's us catch errors
# try: # again indentation after :
#     num = int(input("Please enter an integer pretty please!"))
#     # next line will only RUN if int conversion in previous line worked
#     print(f"Thank you square of {num} is {num**2}")
# except ValueError: # best practice is to catch specific errors
#     print("You did not enter a valid integer!")
# we could catch more errors here

# better to insert try insert while if we want to ENSURE valid input
while True: # so forever ask for input
    try: # again indentation after :
        # inside try we perform something that could throw an error
        # we catch that error with except below
        num = int(input("Please enter an integer pretty please!"))
        # next line will only RUN if int conversion in previous line worked
        print(f"Thank you square of {num} is {num**2}")
        break # we are guaranteed to have an num with valid int conversion here
    except ValueError: # best practice is to catch specibreafic errors
        print("You did not enter a valid integer!")
        print("Please try again ;)") # returns to while True
    
print("Rest of program starts") # now num is guaranteed to be int!
print("num is value", num, "and its type is", type(num))

