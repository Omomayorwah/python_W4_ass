# 1. Write a Python program to read a file and write its contents to another file with the statement "The following statements are true" at the beginning of the new file.
file = open('assignment.txt', 'r')
file2 = open('assignment2.txt', 'w')
data = file2.write("The following statements are true" + file.read())

# Exception handling
try:
    file = open('user_details.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found or can not be read.")
finally:
    file.close()