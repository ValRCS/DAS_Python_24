# Classes and Objects in Python
# Class is a blueprint for the object.
# Object is an instance of the class.

# Classes describe objects. Objects have attributes and methods.
# Attributes are variables that belong to the object.
# Methods are functions that belong to the object.
# Typically Methods do something with the attributes of the object.

# one reason to learn about classes and objects in Python
# is that it makes it easier to work with large codebases.
# Also in Python almost everything is an object.

# print("Classes and Objects in Python")
# print("type of number 42 is: ", type(42))
# # this means that somewhere Python has this blueprint for an integer object
# # similary for strings
# print("type of 'hello' is: ", type('hello'))
# # this means that somewhere Python has this blueprint for a string object
# # strings have methods which are functions that belong to the string object
# print("Example of upper method of string object: ", 'hello'.upper())

# how could we live without classes and objects?
# imagine that we have a program that needs to keep track of students
# and their grades. We could use a dictionary to store the data.
# student_dict = {"Ansis": [10, 9, 8], "Zane": [7, 8, 9]}
# then we might also want to adjust the grades of the students
# we could write a function to do that
# def add_grade(student_dict, student, grade):
#     student_dict[student].append(grade)
# # and then we could call the function
# add_grade(student_dict, "Ansis", 7.5)
# # also we could make a function to print all grades for some student
# def print_grades(student_dict, student):
#     print(student_dict[student])
# print_grades(student_dict, "Ansis")

# the issue/problem with above approach is that it is not very scalable for larger
# codebases. It is hard to keep track of all the functions and dictionaries.
# we would have to search through our code for appropriate functions and dictionaries.

# instead let's do a class for a simple student class without __init__ method

class SimpleStudent:
    age = 21 # I've defined an attribute age
    name = "Bozo" # I've defined an attribute name
    # also I've defined some methods
    def print_age(self): # self is a reference to the object itself NOT class
        print(self.age)
    def years_pass(self, n = 1): # n is a default parameter
        self.age += n

new_student = SimpleStudent()
print("new_student age: ", new_student.age)
# i could also call method
new_student.print_age() # note we do not need to pass self here it is automatically passed!!!
# let's pass a year
new_student.years_pass()
new_student.print_age()

another_student = SimpleStudent() # this is a new instance/object of the class SimpleStudent
# what age will he/she be?
print("another_student age: ", another_student.age)
# i could get name of the student
print("another_student name: ", another_student.name)
# how about original student?
print("new_student name: ", new_student.name)
# let's change name of the student
new_student.name = "Ansis"
print("new_student name: ", new_student.name)
# what about another_student?
# Baiba is still Bozo
# let's change name of another_student
another_student.name = "Baiba"
print("another_student name: ", another_student.name)
# so 3 years pass for Baiba
another_student.years_pass(3) # 3 years pass for Baiba
print("another_student age: ", another_student.age)

# there is one downside to SimpleStudent class it is that all students have the same age
# also they have same name to start with
# much better would be to initialize the object with age and name

# let's do a class for a student class with __init__ method
# __init__ method is a special method that is called when an object is created

class Student:
    # __init__ is so called dunder method
    # dunder stands for double underscore
    # full list of dunder methods can be found here:
    # https://docs.python.org/3/reference/datamodel.html#special-method-names
    def __init__(self, name, age=21, grades=()): # __init__ method is called when object is created
        # note that defaults should be immutable objects like None, True, False, numbers, strings, tuples
        # do not use mutable objects like lists, dictionaries, sets for defaults!
        # we can pass in any type of object such as list or dictionary, but not use mutable objects as defaults
        print("Creating new student")
        self.name = name # name is an attribute of the object
        self.age = age # age is an attribute of the object
        self.grades = list(grades) # grades is an attribute of the object
        # if we passed in list of grades then nothing bad will happen if we call in list or tuple
        # note that incoming name and age are not the same as the attributes
        # the names could be different but it is a good practice to keep them the same
        self.print_age() # note I can call method that I declared below
        # with normal functions I would need to have function declared before I call it
        print("New Student Created: ", self.name, self.age)

    def print_grades(self):
        print(f"Printing grades for {self.name}: {self.grades}")

    # let's make a method to calculate average grade
    def average_grade(self):
        # let's add a sanity check - newspeak is to call this soundness check
        if len(self.grades) == 0:
            print("No grades for student")
            return 0 # could return None or -1 or something else
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade):
        self.grades.append(grade)
        return self # so we return the object itself
    
    # methods that have nothing useful to return should return self
    # then we can chain methods
    # we could add method to print average grade
    def print_average_grade(self):
        print(f"Average grade for {self.name}: {self.average_grade()}")
        return self # so we return the object itself

    def print_age(self): # self is a reference to the object itself NOT class
        print(self.age)
        return self # so we return the object itself
    def years_pass(self, n = 1): # n is a default parameter
        self.age += n
        return self # again we return the object itself
    

# let's create a new student
new_student = Student("Ansis", 21) # so we pass name and age to the __init__ method of the class
# let's print the age of the student
new_student.print_age()
# another student
another_student = Student("Baiba", 22)
# let's print the age of the another student
another_student.print_age()
# now that we have default parameter for age we can create a student without age
third_student = Student("Zane") # Zane will be automatically 21 years old
# let's create another student with name staring with C
fourth_student = Student("Cecilija", 23, [10, 9, 8]) # Cecilija will be 23 years old with grades 10, 9, 8
# note it is completely fine to pass in list of grades or tuple of grades
# let's print grades of the fourth student
fourth_student.print_grades()
# let's calculate average grade of the fourth student
print("Average grade of the fourth student: ", fourth_student.average_grade())
# how about Ansis?
print("Average grade of the new student: ", new_student.average_grade())
# now I can print average grade of the fourth student
fourth_student.print_average_grade()

# now how about storing these students in some structure?
# we could store them in a list or a dictionary or set or another object of type MyClass

# how about a list
students = [new_student, another_student, third_student, fourth_student]
# let's print all grades for these students
print("Printing all grades for all students")
for student in students:
    student.print_grades()
    student.print_average_grade()

# let's add some grades to ansis
# i could make alias for ansis
ansis = new_student # this is NOT copy this is just a shortcut
#now we can see the usage of self
# because all of the below methods return self we can chain them
# last one could return anything or None
ansis.add_grade(10).add_grade(9).add_grade(8).add_grade(5).print_average_grade().print_grades()
# we could of course do this by calling each method separately
# but chaining is more elegant

# already we can see that maybe we would want to store Courses or Classes for student not just a simple list
