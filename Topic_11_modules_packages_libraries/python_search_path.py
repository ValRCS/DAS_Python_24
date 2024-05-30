# let's find out the order Python searches for modules

import sys # standard library module
print(sys.path) # list of directories where Python searches for modules

# this leads to important conclusion
# do not name your files the same as standard library modules ! :)
# if you do you will lose ability to import that standard library module