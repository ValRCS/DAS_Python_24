# let's find out the order where Python looks for modules

# Python has a certain order in which it searches for modules
import sys  # standard library module
print(f"Packages search path: {sys.path}")
# so we can see that Python will first look in the current directory
# how do we find our current directory?
# import os
# print(f"Current working directory: {os.getcwd()}")

# so if python looks in current directory first
#  we can have a file with the same name as a standard library module
# so avoid file names such as string.py, math.py, sys.py etc.