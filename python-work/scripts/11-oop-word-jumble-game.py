# Do the following modifications:
# Give the user a second chance - give a hint in the second chance
# Example: apples -> this is a fruit
# first chance -> offer 2 points
# second chance with hint -> offer 1 point
# Key challenge: how to store the hints


import random

class wordJumbleGame:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.words = [ "apples", "laptop", "mercedes", "carrot", "mobile"]

    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def run(self):
        self.points = 0
        random.shuffle(self.words)

        # Welcome message
        print("Hi! ", self.name, " let\'s play Word Jumble Game")

        # pick a word, repeat the process for all words
        for word in self.words:
            # jumble the word
            jword = self.jumble(word)

            # show the word and as the user to input the actual word
            print("-> ", jword)
            uword = input("Can you guess? ")

            # compare the user input word with the chosen word
            # awards points accordingly
            if(uword == word):
                print("Correct!")
                self.points += 1
            else:
                print("Incorrect")

    def results(self):
        if(self.points > 3):
            print("Excellent playing")
        else:
            print("Better luck next time")


# --------------------------------------------------------------------------

p = wordJumbleGame("Anil")
p.run()
p.results()

# --------------------------------------------------------------------------

names = ["Hruday", "Jahnavi", "Laya"]
gameObjects = [wordJumbleGame(name) for name in names]

for obj in gameObjects:
    obj.run()

for obj in gameObjects:
    print('-'*60)
    obj.results()
