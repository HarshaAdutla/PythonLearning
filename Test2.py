
# Lists
"""
List data type is not mutable. Means We can modify the list values again if we want.
Tuples are mutable. Means once we declare the values in it, we can't do any modification to the values.
List will be enclosed with square brackets ' [] '
"""


values = [1, 2, "It is a String", 2.31]
# List is a data type that allows multiple values and can be different data types
print(values[0])        # index will start from 0 in lists
# Output is : 1

print(values[-1])       # It will print the last value
# Output is : 2.31

print(values[1:3])      # It will start print values from 1 index to 3 index output is 2, "it is a string
# Output is : [2, 'It is a String']

values.insert(3, "Hello")   # Here we can add values to list using insert operation, It will be added in 3rd index
print(values)
# Output is : [1, 2, 'It is a String', 'Hello', 2.31]

values.append("End value")     # Here append will add the value at the last in the list
print(values)
# Output is : [1, 2, 'It is a String', 'Hello', 2.31, 'End value']

values[2] = "Updated String"    # Here we are updating the second value so previous value wil be overwritten
print(values)
# Output is : [1, 2, 'Updated String', 'Hello', 2.31, 'End value']

del values[1]       # Here it will delete the first index value ( 2 is removed from the list)
print(values)
# Output is : [1, 'Updated String', 'Hello', 2.31, 'End value']



# ______________________________________________________________________________________________________________________