### Page 197
## 10-1. Learning Python
# Reading the entire file
filename = 'learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# Looping over the file object
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Storing the lines in a list
filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
line_string = ''
for line in lines:
    line_string += line.rstrip()

print(line_string)

## 10-1. Learning C
# first one:
line_string.replace('Python','C')