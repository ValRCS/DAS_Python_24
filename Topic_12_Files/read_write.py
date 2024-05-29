# Reading and Writing Files
# Docs: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# Real Python: https://realpython.com/read-write-files-python/

# What is a File?
# A file is a named location on disk to store related information. 
# It is used to permanently store data in a non-volatile memory (e.g. hard disk).
# Idea of persistent storage that outlives the execution of a program.
# files have multiple formats: text, binary, etc.
# text files we define the encoding (e.g. UTF-8, ASCII, etc.)
# binary files are not human readable
# text files can have multiple formats: TXT, CSV, JSON, XML, HTML, PY, etc.
# typically these days we deal with Unicode text files encoded in UTF-8

# File Operations
# 1. Open a file
# 2. Read or write (perform operation)
# 3. Close the file

# first let's determine where we are , where is our working directory
import os # os module provides a way of using operating system dependent functionality
print("Current Working Directory", os.getcwd()) # get current working directory
# this will be important when we use relative paths to read and write files

# one approach is to use full absolute path
abs_path = r"D:\Github\DAS_Python_24\Topic_12_Files\frost.txt" # r ignores escape characters
# Linux and Mac use / and Windows uses \ as path separator
# for windows it is a good idea to use raw string to avoid escape characters
print("Absolute Path:", abs_path)

# let us open this file and read its content
# file = open(abs_path) # open file in read mode - default mode is read
# we need to provide encoding type to read the file if not using ASCII symbols
file = open(abs_path, encoding='utf-8') # open file in read mode
# file is not text, it is a file object - think of stream of data like river
text = file.read() # read the content of the file
# critically we want to close the file after we are done with it
file.close() # close the file
print("Content of the file:")
print(text)
# we see that the file content is read and printed as one big string
# except for the places where we had non ASCII characters
# those look like gibberish

# Negatives to using absolute paths
# 1. Platform dependent
# 2. Hard to manage
# 3. Not portable - difficult to share code with others

# so solution is to use relative paths
# relative paths are relative to the current working directory
relative_path = r"Topic_12_Files\frost.txt"

# let us open this file and read its content
file = open(relative_path, encoding='utf-8') # open file in read mode
rows = file.readlines() # read the content of the file as list of lines
file.close() # close the file

# last 3 rows
print("Last 3 rows of the file:")
for row in rows[-3:]:
    print(row.strip()) # strip removes leading and trailing white spaces

# change working directory
os.chdir(r"Topic_12_Files") # change working directory
# print new working directory
print("New Working Directory", os.getcwd()) # get current working directory

# now that I am in the same directory/folder as the file I can use relative path
file = open("frost.txt", encoding='utf-8') # open file in read mode
text = file.read() # read the content of the file
file.close() # close the file
print("First 50 characters of the file:")
print(text[:50]) # print first 50 characters of the file