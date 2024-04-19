# Program to reverse the input number

# input
userNum = input("Enter an integer: ")

# process/output

if(userNum.isdigit()):
    print("The reversed number is ", userNum[::-1])
else:
    print("The input is not a number")


