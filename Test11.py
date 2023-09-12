
# Strings

str = "Harshavardhan Reddy"     # This is an Example string

print(str[1])       # Extracting characters using index
# Output is : a

print(str[0:6])     # Printing a substring using from and to indexes
# Output is : Harsha


# We can not concatenate a string with an integer
# To concatenate a string and integer we can use the formate method like below

name = "Harsha"
age = 26

statement = "{} {}".format(name, age)   # We are concatenating the string and integer and storing it in a variable
print("Statement is : " + statement)
# Output is : Statement is : Harsha 26


# We can concatenate two strings directly
str1 = "Harshavardhan "
str2 = "Reddy"

name = str1 + str2

print(name)
# Output is : Harshavardhan Reddy


# Checking the substring

stringOne = "Harshavardhan Reddy"
stringTwo = "Reddy"

print(stringTwo in stringOne)       # line 34 and 35 both works
print(stringOne.__contains__(stringTwo))    # These two line (34 & 35) will print true or false as result
# Output is : True


# Split (Splitting a string)

email = "harsha.adutla@gmail.com"
# Here I am trying to split the above string based on the dot ' . '
var = email.split(".")
print(var)    # This will separate the sting and gives out put in a list
# Output is : ['harsha', 'adutla@gmail', 'com']

# If I want first value in the list I will print it using index
print(var[0])
# Output is : harsha



# Trim
"""
Trim is used to remove the white spaces in the beginning and ending (leading and trailing) of a string.
In python we can not directly use trim, we need to use one method which is strip.
"""
stringThree = " It is Great    "
value = stringThree.strip()
print("Values before trim is :" + stringThree)  # Output is : Values before trim is : It is Great
print("Value after trim is: " + value)
# Output is : Value after trim is: It is Great

# If we want to remove only the beginning white spaces not the ending white spaces then we need to lstrip( leftstrip)
print(stringThree.lstrip())
# Output is : It is Great

# Similarly if we want to remove the ending white spaces then we need to use rstrip (rightstrip)
print(stringThree.rstrip())
# Output is :  It is Great      White space at the beginning is still there


