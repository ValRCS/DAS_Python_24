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

# we have a better way of closing the file using with statement
# with is so called context manager
with open("frost.txt", encoding='utf-8') as file:
    text = file.read() # read the content of the file
    another_text = file.read() # read the content of the file again...?
    print("Another Text:", another_text) # this will be empty string
    # empty string because reading file is like playing a record
    # we have a needle that is at the end of the record
    # if for some strang reason you want to read the file again
    # you can use seek method to move the needle to the beginning
    file.seek(0) # move the needle to the beginning of the file
    # we could seek to any position in the file
    # file.seek(100) # move the needle to the 100th character
    another_text = file.read() # read the content of the file again
    print("Another Text:", another_text[:50]) # this will be the full text
    # again it is rare to want to read file again
    # seek is for those cases when we have some strange file format
    # and we need to manipulate the file pointer
    # file is still open here
# file is automatically closed after the with block

# so again best practice is to use with statement
# use utf-8 encoding for text files
# use read method to read the content of the file or readlines to read lines

# again
with open("frost.txt", encoding='utf-8') as file: # mode='r' is default
    text_lines = file.readlines() # read the content of the file
    # readlines preserves the new line characters!
# file is closed now we can do some analysis or any regular text processing

# now that we have text_lines we can do some processing
# let's remove first 3 lines
text_lines = text_lines[3:]
# now I want to remove all rows that start with number or only have whitespace

# for now let's use just regular list and string methods and for loop
cleaned_text_lines = []
for line in text_lines:
    if line.strip() and not line[0].isdigit():
        # so line has to have SOMETHING after strip and first character is not digit
        cleaned_text_lines.append(line)

# how many original lines do we have
print("Number of original lines:", len(text_lines))

# how many cleaned lines do we have
print("Number of cleaned lines:", len(cleaned_text_lines))

# let us save the results to a new text file
output_file = "frost_cleaned.txt"
with open(output_file, mode='w', encoding='utf-8') as file:
    file.write("CLEAN POEM\n") # note newline character
    # you could use print function to write to the file
    # print is heavier(slower) than write, so use write if you can
    print("New Line", file=file) 
    # here we can start writing to the file
    file.writelines(cleaned_text_lines)
    # here we can stop writing to the file
# file stream is closed now

# NOte we could open file in read and write mode but it is better to open in write mode separately
# this way we avoid accidentally overwriting the file

# there is 3rd mode 'a' for append - we can append ONLY at the end of the file
# let's add timestamps to the file
import datetime
with open(output_file, mode='a', encoding='utf-8') as file:
    file.write("\n")
    file.write("Timestamp: ")
    file.write(str(datetime.datetime.now()))
    file.write("\n")
    # # we could use print function to write to the file
    # print("Timestamp:", datetime.datetime.now(), file=file)
# file is closed now

# now let's think why is there only one timestamp after appending to the file?

# reason is that we opened the file in write mode before appending
# write always deletes the content of the file before writing

# so general principle for reading and writing files

# 1. use with statement to open and close the file
# 2. use utf-8 encoding for text files - 99% of the time
# 3. use read method to read the content of the file or readlines to read lines
# 4. use write method to write to the file

# if you need to append to the file use 'a' mode

# for binary files we use 'rb' and 'wb' modes - discuss later

# how to check if file exists?
# new way it to use Path object from pathlib module
from pathlib import Path
file_path = Path(output_file)
if file_path.exists():
    print(f"File {file_path} exists")
else:
    print(f"File {file_path} does not exist")

# Path is very powerful has many methods for working with files and directories

# let's search for all .txt files in the current directory ONLY
# we can use rglob method
for file_path in Path(".").glob("*.txt"): # no looking in subdirectories
    # . means current directory
    print(file_path)

# let's get all text files in the parent directory and all its subdirectories
text_files = list(Path("..").rglob("*.txt")) #  .. is parent directory
print("Text Files in Parent Directory and Subdirectories:")
print(text_files)
