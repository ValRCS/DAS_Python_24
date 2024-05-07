# we use Booleans to make decisions on what to do
a = 200
b = 4
# we use if then Boolean value to crate code blocks
# that execute conditionally based on that Boolean
if a < b:
    # note that after : Thonny automatically generated indentation
    # note the Indentation! typically it is 4
    # you can change default indentation to 2 or less commonly 8
    print("a is less than b ?", a < b)
    print("a is actually", a)
    print("b is actually", b)
    # still inside if code block
# we are outside now normal indentation
print("This will always run!")

# often we want to split our work in two exclusive paths
# either do one or another but not both or none
a = 4
if a > b:
    print("Oh a > b indeed")
    print("a, b", a, b)
else: # here it means a <= b
    print("a must be equal or less than b")
    print("a b", a, b)
    # we are still inside else branch of if else block
# normal block

# we can create longer if else if else if else chains
c = 100
d = 200
f = 300
if a > b:
    print("cool a > b", a, b)
    if c < d:
        print("aha c < d", c, d)
    else: # means c >= d
        print("oho c >= d", c, d)
else: # for a <= b
    print("means a <= b", a, b)
    # we could check anything here
    if c < d < f:
        print("Cool c < d < f", c, d, f)
    else: # not true that c < d < f
        print("Apparently NOT c < d < f", c, d, f)
# so Python solves the dangling else problem using indentation
# each else corresponds to if that is same level of indentation

# overall try to make your if else chains as flats as possible
# it makes debugging easier

# all nested ifs can be rewritten flatly
# might need more thinking about code

# one examle of flat if else if else would be we have 3 roads needed
print("will check a and b with if elif else block")
if a > b:
    print("a > b", a, b)
    # we can do more stuff when a > b here
elif a < b:
    print("a < b", a, b)
    # we can do more stuff when a < b here
else: # by process of elimination we end up here only when a == b
    print("Only possibility that a equals b", a, b)
    # we can do more stuff for when a == b
# back to normal flow
print("Whew all done")

    