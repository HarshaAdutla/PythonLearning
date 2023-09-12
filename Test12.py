
# File Operations

# We have some data in Text.txt file, and now we are extracting the data from that file

file = open('Text.txt')     # Here we are opening the Text file and creating an object to it (file)
print(file.read())     # It will read all the content of file
# Output is :
# Viswamohan Reddy
# Harshavardhan Reddy
# Siva sudheer Reddy
# Pavan kumar Reddy
print(file.read(2))     # It will read first two characters of the file
# Output is : Vi


file.close()


"""
When we open a file make sure that we are closing the file after usage.
"""