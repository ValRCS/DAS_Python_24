# filozofiski while cikls ir pielāgots ciklošanai
# kad nezinam konkrētu galu
# ja zinam konkrētu skaitu tad mums ir for cikls
print("Let the for looping start!")
# so if we want to do something 5 times with for in loop
# here we use range(5) to go through numbers from 0 to 4 included
# note we did not have to declare i beforehand
for i in range(5): # we go through half-baked generator of numbers from 0 to 4 included
    print("i is i",i)
    # still inside loop going back to start
print("outside i is now",i)

# we can reuse i again (or used different name)
for i in range(10,15): # so from 10 to 14 included
    print("i is i",i)
    # still inside loop going back to start
print("outside i is now",i)

for i in range(30,50,2):
    print("i is i",i)
    # still inside loop going back to start
print("outside i is now",i) # i will be...48!

# so range has syntax range(start,stop(exclusive), step)
for i in range(100,90, -2):
    print("i is i",i)
    # still inside loop going back to start
print("outside i is now",i) # 92 !

# range does not let you have fractional, floating point numbers
# for that we could use while loop with manual start, stop, step
# alternatively better way would be to use NumPy external library which offers fractional increments

# for in essentially goes through SOME COLLECTION of items
name = "Valdis"
for c in name: # typical to use c for character
    print("Working with letter", c)
    
my_emoji = "👨‍🎓👩‍🎓🤓🎓🏫✍👨‍💼👩‍💼🧑‍💻👩‍💻📚🎒" # so string is just a collection of individual
# let's print out their Unicode code points
for emoji in my_emoji: # so we will have access to emoji one by one
    print("Emoji", emoji, "Unicode number", ord(emoji))
    
# we could use index with [] notation to access individual symbols
# however Pythonic way is to use enumerate
for i, c in enumerate(name): # enumerate is built into Python
    # so i will start with 0, and c will have whatever character is first
    print(f"No.{i} -> symbol {c} -> its Unicode {ord(c)}")
    
# now what some call Python's for loop mistake
# rare but possible to use
# we can break from for loops that is normal and not weird
for i in range(10):
    print(i)
    if i == 4044: # maybe we have different variable to compare
        print("i is 4?", i)
        break # we break free early
else: # this is the weird else it is attached to for loop not if
    # it means for loop(and also while) finished WITHOUT break
    print("Finished for loop normally", i) 
print("after break i is", i)