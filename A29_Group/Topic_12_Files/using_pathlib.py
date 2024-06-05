# pathlib offers a more object-oriented approach to working with files and directories.
# main objects is Path
# Path is useful if you expect to work on multiple OSes
# such as Windows, Linux, MacOS
# usually we import it as follows
from pathlib import Path
# let's find out the list of all files in the current directory
# current directory is where the script is

files = [f for f in Path(".").iterdir() if f.is_file()]
print("Files in the current directory:")
print(files)

# now let's find the files in the directory of the script
# we can use __file__ to get the path of the script

files = [f for f in Path(__file__).parent.iterdir() if f.is_file()]
print("Files in the directory of the script:")
print(files)

# let's use Path to find txt files in the current directory
txt_files = list(Path(".").glob("*.txt"))
print("Text files in the current directory:")
print(txt_files)
# let's find ALL text files in current directory and subdirectories
txt_files = list(Path(".").rglob("*.txt"))
print("Text files in the current directory and subdirectories:")
print(txt_files)
# txt_files is a list and you can open each file with open function
# or use context manager with open

# there are also file copy and move methods
# for that there is module shutil
# Docs: https://docs.python.org/3/library/shutil.html
