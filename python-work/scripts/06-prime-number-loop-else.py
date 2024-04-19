# Program to input a number and detect if it is prime or not

# input
n = int(input("Enter a number: "))

# process/output

for i in range(2, n):
    if(n % i == 0):
        print("Then number is not prime")
        break
else:
    print("The number is prime")