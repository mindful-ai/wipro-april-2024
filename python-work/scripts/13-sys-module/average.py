# This program demonstrates how to  pick-up values from the command line
# Usage: python .\average.py 10 20 30 40 50 60

import sys

print(sys.argv)

print("File name: ", sys.argv[0])

avg = sum([ int(d) for d in sys.argv[1:]])/len(sys.argv[1:])
print("Average : ", avg)