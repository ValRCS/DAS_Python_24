# let's make a small application
# that adds up numbers until user enters "q"

total = 0
user_input = "" # we need some user input to compare
while True:
    try:
        user_input = input("Enter number or letter q to quit and press enter")
        #above line is going to give you string after enter
#         if user_input == "q":
        if user_input.lower().startswith("q"): # works for QUIT , quit , q, Quitter, QWERTY etc
            print("Okay let's leave")
            break
        number = float(user_input) # here you could get an error
        # here we are guaranteed to have a number that contains a float!
        total += number
        print("You entered", number)
        print("Total is now", total)
    except ValueError:
        print("Please enter a number!")

