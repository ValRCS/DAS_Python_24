# Python offers a way of specifying the types of parameters and return values
# for example let's say I want to specify that my function will take two integers and return an integer
# def add(a: int | float | str, b: int | float | str) -> int | float | str:
#     return a + b # not completely correct Type hint since we do not want to allow str + int 
def add(a: int, b: int) -> int:
    return a + b

# works as expected
print(add(5, 6))

# however Python does not enforce these types
# so I can still pass a string
print(add("Valdis", "Rūta"))

print(add(5.5, 6.6)) # works but returns a float

# we can specify that we want say a list of integers
def sum_list(input_list: list[int | float], greeting: str = "Let's rock!") -> int | float:
    print(greeting)
    return sum(input_list)

print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([1, 2.5, 3, 4, 5]))