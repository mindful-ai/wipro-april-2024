# Program to create a character triagle
# input:
#   c -> character (*)
#   l -> 3
# output:
#   *
#   **
#   ***

# input
print("This program prints a character triangle")
ch = input("Enter the character: ")
lines = int(input("Enter number of lines: "))

# process/output

for i in range(lines, 0, -1):
    print(ch*i)