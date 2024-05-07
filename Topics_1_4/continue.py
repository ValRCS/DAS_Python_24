# we also have continue less used than break
# continue GOES back immediately to start of loop

i = 0
while i < 10:
    print(i)
    # important to increment BEFORE continue call
    i += 1
    if i % 2 == 0:
        print("Even number going back to start",i)
        continue # jumps to line 5 and checks i < 10 again
    # if i did not have continue I could emulate it with else here
    print("doing something with odd number",i)
    