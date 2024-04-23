import mymodule


print("projectB.py -> __name__ =", __name__)

# Program to determine if a input number is prime or not

# input
n = int(input("Enter a number: "))

# process
flag = True
for i in range(2, n):
    if(n % i == 0):
        flag = False
        break

# output
if(flag):
    print("The number is prime")
else:
    print("The number is not prime")