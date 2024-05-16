# Python lets you write documentation for your functions using docstrings

# docstrings are written between triple quotes

# docstrings are not comments, they are accessible through the __doc__ attribute of the function

# we can combine docstrings with type hints

# let's write a function that takes two integers and returns their sum
def add(a: int, b: int) -> int:
    """
    This function takes two integers and returns their sum

    Parameters:
    a (int): the first integer - could show limitations or constraints
    b (int): the second integer

    Returns:
    int: the sum of the two integers - could show expected return value
    """
    return a + b

# now we can access the docstring
print(add.__doc__)
# more importantly we can hover over the function in an IDE and see the docstring

print(add(5, 6))

# docstrings can also be parsed by tools like Sphinx to generate documentation
# Sphinx is a tool that makes it easy to create intelligent and beautiful documentation
# for Python projects (or other documents consisting of multiple reStructuredText sources)
# URL: https://www.sphinx-doc.org/en/master/index.html