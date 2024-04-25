# Design the word jumble game
# -> A L E S P P
# -->>  JA:LKSD
# Incorrect
# -->> A P P L E S
# Correct

import random

def jumble(word):
    temp = list(word)
    random.shuffle(temp)
    return ''.join(temp)

words = [ "apples", "laptop", "mercedes", "carrot", "mobile"]
random.shuffle(words)

points = 0

# pick a word, repeat the process for all words
for word in words:
    # jumble the word
    jword = jumble(word)

    # show the word and as the user to input the actual word
    print("-> ", jword)
    uword = input("Can you guess? ")

    # compare the user input word with the chosen word
    # awards points accordingly
    if(uword == word):
        print("Correct!")
        points += 1
    else:
        print("Incorrect")

# finally print the result

if(points > 3):
    print("Excellent playing")
else:
    print("Better luck next time")


'''
Questions:

1. How will do a detailed test of this logic?
2. How will you make it into a multi-player game?

'''