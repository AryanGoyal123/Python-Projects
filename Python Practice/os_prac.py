import os

"""
The os module in Python provides a way to interact with the operating system. 
It offers a portable way to use operating system-dependent functionality.
"""

# Prints the name of all the files in the directory
for file in os.listdir():
    print(file)

# get current working directory
print(os.getcwd())

# os.mkdir(path): Creates a directory named path with numeric mode mode.
# os.rmdir(path): Removes (deletes) the directory path.
# os.remove(path): Removes (deletes) the file path.

if os.path.exists('args.py'):
    print("It exists")
else:
    print("Does not exist")

# This method joins various path components
print(os.path.join("/tmp", "myfile.txt"))

size = os.path.getsize('scope_prac.py')
print(f"Size in bytes: {size}.")

# use the .. to go back up a directory in your tree
path = '../Python OOP Projects/School Management Project'
print("#####")
for file in os.listdir(path):
    print(file)
