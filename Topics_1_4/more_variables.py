# DRY princips - Do Not Repeat Yourself
# Python mainīgos mēs nedeklarējam atsevišķi
# Mēs uzreiz sākam mainīgos lietos pēc pirmā =
furniture = "desk"
print(f"I am sitting on a {furniture}")
print("Time to buy some more " + furniture + "s") # already we see a need for some logic here..
paint_job = f"Let's paint some {furniture}s"
print(paint_job)
# again identificators versus string literatals
name = "Valdis"
print(name)
print("name")
friends_name = "Valdis"
print(friends_name)
x = 20  # so x points to value of 20 in memory
y = x**2   # y points to 400 in memory
print(x, y)
print(f"{x} squared is {y}")
y = 5 * x # now y is just 100
print(x, y)
print(f"{y} is 5 times {x} now")
print(name, type(name)) # type let's us see what data type is variable holding
# type has nothing to do with printing!
# type returns the data type of some variable
PI = 3.1415926 # usually this would be constant but not enforced in Python
print(f"Value of PI is currently {PI} and its data type is {type(PI)}")
PI = round(PI, 4) # we will overwrite old PI with new PI
print(PI, type(PI))
PI = round(PI) # default rounding is to 0 digits AFTER comma
print(PI, type(PI)) # now our PI is 3
# related: https://en.wikipedia.org/wiki/Indiana_pi_bill
some_number = 5.89261
some_round_number = round(some_number)
some_int_number = int(some_number)
print(some_number, some_round_number, some_int_number)
# note at this stage we do not know about lists or other complex data types...
a = 1.5
b = 2.5
c = 3.5
d = 4.5
# so in middle we round one edge case UP one edge case DOWN
print(a,b,c,d)
print(round(a), round(b), round(c), round(d))
# anything over .5 will work normally
a = 1.51
b = 2.51
c = 3.51
d = 4.51
print(a,b,c,d)
print(round(a), round(b), round(c), round(d))
a = 1.49
b = 2.49
c = 3.49
d = 4.49
print(a,b,c,d)
print(round(a), round(b), round(c), round(d))
