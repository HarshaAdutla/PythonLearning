
#Tuples
"""
Tuples are similar to the list but immutable. ( Only two difference)
1. Tuples are immutable. Means once we declare the values in it, we can not do any modifications to the values.
2. Tuples will be enclosed with parenthesis ' () '
"""

values = (1, 2, 3, "String", 2.30)
print(type(values))      # Here checking the type
# Output is : <class 'tuple'>

# values[3] = "It is a String"    # Here i am trying to chnage the 3rd index value
# print(values)
# Output is : An error. Because tuple are mutable, we can't modify the data once we declare it.
# ______________________________________________________________________________________________________________________

# Dictionary
"""
Dictionaries will be define in flower brackets.
Dictionaries will have the data in ' key value pair '
"""

a = {1: "First Name", 2: "Second Name", "age": 25, "Name": "Harsh"}
# Here 1 is key and holds a value of ' First Name ' same for keys 2 and 3. If String is used no matter either key or -
# value quotes needs to be used
print(a["age"])     # Here printing the value using its KEY. There is no index identification in dictionaries.
# Output is : 25

print(a["Name"])
# Output is : Harsh

# ______________________________________________________________________________________________________________________

# How to create Dictionaries dynamically at Run time.

dict = {}
dict["First Name"] = "Harsh"        # This key value pair will be added to the dictionary
dict["Last Name"] = "Reddy"         # This key value pair will be added to the dictionary
print(dict)
# Output is : {'First Name': 'Harsh', 'Last Name': 'Reddy'}

# Now we can read the values as usual. One example shown below
print(dict["Last Name"])
# Output is : Reddy

