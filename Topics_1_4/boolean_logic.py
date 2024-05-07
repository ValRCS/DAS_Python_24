# one thing we can do with Boolean valus is to combine them
is_raining = False
is_spring = True
is_sunny = True
# we can use logical conjuction to check whether BOTH values are true
# Python uses English and (not && as other languages), Python does have & for bit operations
print(is_spring and is_sunny)
print("Conjuction in Python we use: and")
print("False and False", False and False)
print("False and True", False and True)
print("True and False", True and False)
print("True and True", True and True) # only one which gives True
# we can create longer chains as well
print(True and True and True and True and 2*2 == 4)
# however one drop of oil spoils the honey!
# this means Python will stop evaluating your conjuction chain
# as soon as it get one False - it looks no further
print(False and True and 5/0 == 500) # 5/0 will not be run
# Python uses lazy evaluation
# so we can divide by 0 if we handle exception
# print(5/0 == 500) # normally 5/0 will produce ZeroDivisionError
# we could handle this error but not now
print("Time for some disjunctions! Python uses: or") # not ||
print("False or False", False or False)
print("False or True", False or True)
print("True or False", True or False)
print("True or True", True or True)
# thus in a long chain of ors, first True will stop evaluation
print(False or False or True or 5/0 == 5000) # again 5/0 will not run

# typically instead of direct True of False those will be some variables or comparison
a = 2
b = 4
c = 10
# so these two are same
print("a < b < c")
print(a < b < c)
print(a < b and b < c) # priority is for < then and
# we are left with negation
print("reverse of is_raining?", not is_raining)
# we have a way of creating a toggle
print("is it raining?", is_raining)
# let's reverse it
is_raining = not is_raining # so we assign the reverse, the TOGGLE
print("is it raining?", is_raining)
is_raining = not is_raining # so we assign the reverse, the TOGGLE
print("is it raining?", is_raining)
is_raining = not is_raining # so we assign the reverse, the TOGGLE
print("is it raining?", is_raining)

