# Program to input a number and detect if it is prime or not

# input
n = int(input("Enter a number: "))

# process
flag = 1
for i in range(2, n):
    if(n % i == 0):
        flag = 0
        break

# output
if(flag == 1):
    print("The number is prime")
else:
    print("The number is not prime")