# Bieži mēs gribam kaut ko darīt atkārtoti
# print("Labdien Maijs!")
# print("Labdien Maijs!")
# print("Labdien Maijs!")

# while construction will run WHILE expression is True
# while True:
#     print("runāja ")

# typically we will have some condition that changes
i = 0
while i < 5: # from 12 I will jump to 18 when i<5 False
    # while block starts here
    print("i is now", i)
    i+=1 # same as i = i + 1
    # still inside
    # I go back to start to while here
# outside while after i<5 is false
print("i will be", i)

floor = 9 # i could have reused i
while floor >= 0:
    print(f"Going down to floor {floor}")
    floor -= 1
    # still inside while loop
print(f"Whew we are finally out on floor {floor}")

# we can use different size steps
cnt = 10
while cnt <= 20:
    print(f"Cnt is now {cnt}")
    cnt += 2 # so cnt = cnt + 2
# cnt is now
print(f"after while loop ends cnt {cnt}")

# let's say I want to run something 1000 times but do not want to show update every loop
i = 0
total = 0
while i < 1000:
    total += i # of course we could use Gauss or sum(range(1000)) for this :)
    # idea is to only show updates every 100
    if i % 200 == 0: # so only -100,0,100,200, ... will return True
        print(f"iteration No. {i} total is now {total}")
    i+=1
# finished
print(f"Final total {total}, iteration {i}")

# let's generalize all of this
START = 100
STOP = 200
STEP = 25
i = START
while i < STOP: # if I add <= STOP then i would end up at STOP+STEP
    print(f"Doing something with {i}")
    i += STEP
    # we could do more work here
    print(f"Doing work after increment when i is {i}")
print(f"All done and i is now {i}")

# hopefully you see that we need a more generalized more concise way of writing definite loops

    
