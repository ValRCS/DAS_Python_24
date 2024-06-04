# matplotlib is one of the largest and oldest libraries for creating visualizations in Python. It is a powerful library that can create a wide range of visualizations, including line plots, bar plots, scatter plots, histograms, and more. 
# In this tutorial, we will learn how to create a simple line plot using matplotlib.

# matplotlib is inspired by MATLAB
# official site: https://matplotlib.org/
# RealPython guide: https://realpython.com/python-matplotlib-guide/
# install with pip install matplotlib

# let's plot a simple square function from 0 to 10
import matplotlib.pyplot as plt
# matplotlib is a big library we only need pyplot module which we rename as plt

# create a list of x values from 0 to 10
x = list(range(11))
# create a list of y values which are the squares of x
y = [i**2 for i in x]
# let's create y2 list which is square of x - 2
y2 = [i**2 - 2 for i in x]

# create a line plot
plt.plot(x, y)
# bar chart
plt.bar(x, y2, color='red')

# add labels to the x and y axes
plt.xlabel('x')
plt.ylabel('y')

# add a title to the plot
plt.title('y = x^2')
# add subtitle
plt.suptitle('This is a simple square function')


# display the plot
plt.show()