# Program that takes number sequence (space separated numbers) from the user
# and separate the odd and even numbers from the sequence
# input:
#   -> 12 34 45 56 67 78 89
# output:
#    odd: 45 67 89
#    even: 12 34 56 78
# pick only integers from user input

# input
print("This program separates the even and odd number from the input sequence")
print("-"*90)

userSeq = input("Enter the space separated sequence of numbers: ")


# process

N = []
temp = userSeq.split()
for item in temp:
    if(item.isdigit()):
        N.append(int(item))

evens = []
odds = []
for item in N:
    if(item % 2 == 0):
        evens.append(item)
    else:
        odds.append(item)



# output
print("-"*90)
print("Odd numbers  -> ", odds)
print("Even numbers -> ", evens)