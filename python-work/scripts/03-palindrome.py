# Program to input a string and check if it is a palindrome

# input
userStr = input("Enter a string: ")

# process/output

if(userStr == userStr[::-1]):
    print("The input string is a palindrome")
else:
    print("The input string is not a palindrome")