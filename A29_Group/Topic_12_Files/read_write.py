# Reading and Writing files
# Docs: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# Real Python: https://realpython.com/read-write-files-python/

# What is a File after all?
# File has a name
# File stores some data
# Files persist data after program ends
# There can be many types of files(txt, csv, json, xml, html, pdf, docx, mp3, jpg, png, exe, zip, etc)
# Many of the above are actually text files, but some are binary files
# Text files are human readable
# Binary files are not human readable - generally
# There can be different types of storage(HDD, SSD, RAM, Network)
# For text files we could have different encodings(ASCII, UTF-8, UTF-16, etc)

# File Operations
# 1. Open a file
# 2. Read or Write (or both) or even append to a file
# 3. Close the file

# Working Path
# first step is to find out where we are
# we can use os module for that
# https://docs.python.org/3/library/os.html
import os
print("Current working directory:", os.getcwd())

# change current working directory to directory where the script is
os.chdir(os.path.dirname(os.path.abspath(__file__))) # pretty old recipe but still works
# now we are in the same directory as the script
print("Current working directory:", os.getcwd())

# to read a file we need to know where it is
# we have two approaches - absolute path and relative path

abs_path = r"D:\Github\DAS_Python_24\A29_Group\Topic_12_Files\frost.txt"
# again i am using r because I am too lazy to escape backslashes such as \\
# on all OS you could also use / instead of \ in paths
# so absolute path uniquely identifies the file on the system

# let's open the file with absolute path
# file = open(abs_path, "r") # read is default not required to specify
# # file is a file object - stream of data from the file
# text = file.read() # read the whole file
# # import to close the file
# file.close() # we will see there is a way to simply close the file without calling close

# if we get UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 0: character maps to <undefined>
# we want to specify encoding
# usually 90% of the time it is UTF-8
# file = open(abs_path, encoding="utf-8") # read is default not required to specify
# text = file.read() # read the whole file
# # file is still open here
# file.close() # we will see there is a way to simply close the file without calling close
# print(text)

# generally we want to use relative path
# relative to the current working directory
# this is much more flexible
# will work across different systems and users

# so we can simply open the file by name without path
# file = open("frost.txt", encoding="utf-8") # read is default not required to specify
# text = file.read() # read the whole file
# # file is still open here
# file.close() # we will see there is a way to simply close the file without calling close
# print(text)

# since closing is a good idea, but we can forget to do it
# for that we can use context manager
# we use with statement
# it will automatically close the file
# with open("frost.txt", encoding="utf-8") as file: # file is a variable name, could f or fin or fstream or anything
#     text = file.read() # read the whole file
#     print("Text length:", len(text))
#     print("File is open:", file.closed)
#     # so I could read more data here right?
#     more_text = file.read()
#     print("More text length:", len(more_text))
#     # why is more_text empty?
#     # historically files come from magnetic tapes and disks
#     # where we have a read/write head
#     # so when we read data we move the head to the end of the file
#     # think of it as needle on the record player
#     # if for some strange reason I want to read file again
#     # i could reset the head to the beginning of the file
#     file.seek(0)
#     more_text = file.read()
#     print("More text length:", len(more_text))
#     # but this is not a common operation
#     # we would use seek if we have a strange file format
#     # and we need to manually skip or go back to some position
#     # most likely your file format is simple and you don't need seek
#     # also here is list of file encodings provided by Python
#     # https://docs.python.org/3/library/codecs.html#standard-encodings
#     # file is still open here
# print("File is open:", file.closed)
# file is already closed here when we go back a level
# print(text)

# often for text lines it can be useful to read all lines
with open("frost.txt", encoding="utf-8") as file:
    lines = file.readlines() # read all lines
# again file is already closed here
print("Number of lines:", len(lines))
print("First line:", lines[0]) # note that lines are separated by \n
print("Last line:", lines[-1])
# last 5 lines
print("Last 5 lines:")
print(lines[:-5])
# so read lines keeps the new line character
# we could strip if rstrip or strip if we don't want it
# however we are likely to write back to the file in any case

# let's do some simple text preprocessing
# first remove first two lines with slicing
lines = lines[2:] # so we replace the list with a new list without first two elements
# now let's remove all rows without text
# we could use row.strip() to remove whitespace and then check if row is empty
# this can be useful if line has extra whitespace
print(f"BEFORE: {len(lines)}")
# clean_lines = [line for line in lines if line.strip()] # this is a list comprehension
# we could do the same with loop
clean_lines = []
for line in lines:
    if line.strip(): #so if not empty, remember that line is not modified
        clean_lines.append(line) # line is added without stripping but could be added stripped
# now we have only lines with text
print("Number of lines after cleaning:", len(clean_lines))
# now let's get rid of rows which start with numbers
# we know that all rows have at least one character so we could simply check first character
# we could also use isdigit method
really_clean_lines = []
for line in clean_lines:
    if not line[0].isdigit(): # isdigit is a string method
        really_clean_lines.append(line)
print("Number of lines after really cleaning:", len(really_clean_lines))
# now we have only lines which don't start with number

# now let's save this cleaned text back to the file
# we will use write mode
# if file exists it will be overwritten in write mode
# if file does not exist it will be created
with open("frost_clean.txt", mode="w", encoding="utf-8") as file:
    file.writelines(really_clean_lines)
    # i could add some extra text here if I want
    file.write("\nHello mom!\n")
    # i could even use print function
    print("Hello dad!", file=file) # note how I pass file argument
    # print is slower than write, but it is more convenient
    # print is slower because it offers more features, formatting, etc
# again file is closed here
# we can not write anything else here to file

# there is another mode - called append
# append lets us add to the end of the file
# if we want to add to the beginning or middle we need to read the file, modify it and write it back

# let's add a timestamp to the file
from datetime import datetime
now = datetime.now()
# let's format the date in format YYYY-MM-DD HH:MM:SS
timestamp = now.strftime("%Y-%m-%d %H:%M:%S") # so - and : are just regular characters
# more on time formatting here: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# let's add the timestamp to the file
with open("frost_clean.txt", mode="a", encoding="utf-8") as file: # note the mode
    file.write(f"Timestamp: {timestamp}\n")

# why is only a single line added?
# because we always overwrite the file in write mode when we saved the really_clean_lines

# we could create a new file with timestamp let's just use month, day, hour, minute
postfix = now.strftime("%m_%d_%H_%M")
file_name = f"frost_clean_{postfix}.txt"
# could save to custom file name
# with open(file_name, mode="w", encoding="utf-8") as file:
#     file.writelines(really_clean_lines)
#     file.write(f"Timestamp: {timestamp}\n")


# we have an option to open two file streams at once
# this can be useful if we want to read from one file and write to another
# and the read file is large and we don't want to load it all into memory

src = "frost.txt"
dst = "frost_almost_clean.txt"
with open(src, encoding="utf-8") as src_file, open(dst, mode="w", encoding="utf-8") as dst_file:
    # both files are open here one for reading one for writing
    for line in src_file: # note that I am not reading all lines at once I am iterating over them
        # i could add some extra logic here if I want
        # if row is empty i could continue the loop
        if not line.strip():
            continue # no need to write empty lines
        if not line[0].isdigit(): # if line is empty it will have first character as \n
            dst_file.write(line)
# both files are closed here

