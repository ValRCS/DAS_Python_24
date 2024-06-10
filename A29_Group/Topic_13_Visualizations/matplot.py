# matplotlib is a plotting library for the Python programming language 
# and its numerical mathematics extension NumPy.

# matplolib and Numpy are not part of standard library, so we need to install them
# official site of matplotlib: https://matplotlib.org/
# Real Python guide to matplotlib: https://realpython.com/python-matplotlib-guide/
# to install we use pip
# pip install matplotlib from command prompt

# pip is a package-management system written in Python used to install and manage software packages.

# pip freeze command is used to list all the installed packages in the current environment.
# typically we use pip freeze to write to requirements.txt file
# pip freeze > requirements.txt

# then we can install all requirements from requirements.txt file
# with command pip install -r requirements.txt

# there is also an alternative package manager called conda
# conda is more powerful than pip, because it can install packages from different sources
# conda also tends to be more curated, because it is part of the Anaconda distribution

# now that we have installed matplotlib we can import it
import matplotlib.pyplot as plt
# plt is very common alias for matplotlib.pyplot

# let's plot x and y values
# x will be in range from 0 to 12 with step 1
# y will be x squared + 5 in other words f(x) = x^2 + 5
x = list(range(13)) 
y = [i**2 + 5 for i in x] # list comprehension
# let's also create y2 which will be simple squares of x
y2 = [i**2 for i in x]

# let's plot a line plot
plt.plot(x, y)
# now let's create a green bar chart
plt.bar(x, y2, color='green')
# let's add x and y labels
plt.xlabel('x')
plt.ylabel('y')
# let's add a title
plt.title('Line plot and bar chart')
# let's draw an arrow from (3, 20) to (3, 50)
# arrow thickness is 3
# color would be red
# head width is 10

plt.arrow(3, 20, 0, 30, head_width=0.5, head_length=5, fc='red', ec='red', lw=3)
# more documentation examples:
# https://matplotlib.org/stable/gallery/index.html

# now we can show it
plt.show() # program will stay open until we close the plot window