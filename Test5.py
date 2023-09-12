# For loop

values = [1, 2, 3, 4, 5, 6, 7]

for i in values:
    i = str(i)
    print("Values is:" + i)
    if i == "5":
        print("Met the value 5 here.")

# Here I am trying to print the list values with multiple of 2

values = [1, 2, 3, 4, 5, 6, 7]

for i in values:
    j = i*2
    # print(i*2)    # This also prints the values with multiple of 2.
    multiple = str(j)
    print("Values after multiplication is:" + multiple)
# ______________________________________________________________________________________________________________________

# Sum of First five natural Numbers ( 1+2+3+4+5 = 15)
summation = 0
for j in range(1, 6):   # If range is (i, j) then it will iterate it from i to j-1. i.e it iterates 1 to 5.
    # print(j)    # Printed th enatural numbers.
    summation = summation + j
summation = str(summation)
print("Sum of first five natural numbers is:" + summation)      # We can not cancatinate the string with integer so in -
# above step I have changed it ot string
# Output is : Sum of first five natural numbers is:15

# ______________________________________________________________________________________________________________________


# Here i am printing the numbers with index difference
print("********")       # Just to Make difference in the output
for i in range(1, 10, 2):   # Here 2 in the range box is the difference box (In jav we mention diff as i++).
    print(i)        # In above, it prints values from 1 to 9(limit is 10) with 2 index difference.
# Output is :
# 1
# 3
# 5
# 7
# 9

# Here we are not providing the initial value bydefault it will treat 0 as initial value.
print("****SKIPPPING THE INITIAL VALUE****")
for i in range(10):     # It will print all natural numbers up to 9
    print(i)
