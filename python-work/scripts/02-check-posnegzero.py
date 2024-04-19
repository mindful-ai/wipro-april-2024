# Program to subtract two numbers and determine if the result
# is positive, negative or zero

import math

# input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# process
res = a - b

# output
print("Difference: ", math.fabs(res))
if(res > 0):
    print("The result is positive")
elif (res < 0):
    print("The result is negative")
else:
    print("The result is zero")

