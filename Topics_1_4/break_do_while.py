# we can break out of loops early

i = 0
while i < 10:
    print("i is",i)
    i+=1
    # i have an option to break out of loops at any point
    if i > 5:
        print("Time to break early")
        break # goes to line 12 immediately
    print("Still inside loop", i)
    
print("All done i is",i)

i = 0
import random
while i < 10_000: # _ is just sintetic sugar
    dice_throw = random.randint(1,6) # 1 to 6 INCLUSIVE - rare to have inclusive
    print("I threw", dice_throw)
    if dice_throw == 6:
        print("nice 6 you have", dice_throw)
        print("Breaking free on iteration ",i)
        break
    i+=1
print("We are freeeee")

# we can use while True with break
# typical for application main loop
i = -90_000_123 # any big number
# I call this loop "shoot first and ask questions later"
# in CS it is called do while loop - runs at least once
# Python does not have do while construction we just emulate it using while
while True:
#     print("running forever or am I?",i)
    if i % 1_000_000 == 0:
        print("i is ", i)
    # so above line will run at least ONCE
    if i > 4:
        print("Breaking free", i)
        break
    i+=1
# free from loop
print("after break i is", i)