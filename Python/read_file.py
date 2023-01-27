# read file in python
import os

absolute_path = os.path.dirname(__file__)
relative_path = "data/file.txt"
full_path = os.path.join(absolute_path, relative_path)

# open file in read mode
with open(full_path, 'r') as file:
    # read all lines at once
    all_of_it = file.read()
    print(all_of_it)

    # seek back to the beginning and read line by line
    file.seek(0)
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

    # seek back to the beginning and read the file into a list
    file.seek(0)
    lines = file.readlines()
    print(lines)