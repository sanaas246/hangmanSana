# HANGMAN PROJECT BY SANA

import random

# Hangman Appearance
stages = ["", "________", "________\n|  |", "________\n|  |\n|  | ", "________\n|  |\n|  | \n|  0 ", "________\n|  |\n|  | \n|  0 \n| /|\ ", "________\n|  |\n|  | \n|  0 \n| /|\ \n| / \ ", "________\n|  |\n|  | \n|  0 \n| /|\ \n| / \ \n| \nYOU LOST!"]

# List of Words, blank spots and the wrong letters
words = "l i o n,t i g e r,g o a t,h o r s e,d o n k e y,d o g,c a t,p i g".split(",")
slots = []
wronglet = []

# FUNCTIONS
# pick a word from the words list
def getWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex].split(" ")

# assess guesses (main function)
def assessGuesses():
    # clear the console
    slots.clear()
    wronglet.clear()
    phase = 0
    # pick a word and print its slots
    word = getWord(words)
    openspots(word)
    # loop to continue guessing
    loop = True
    while loop:
        guess = input("\nPick a letter: ")
        if guess.isalpha() and len(guess) == 1:
            if guess in slots: 
                print("You have already guessed that!")
                print(slots)
                print(stages[phase])
            elif guess in word:
                print("Correct\n")
                gueIndex = search(word, guess)
                correct(word, gueIndex)
                print(stages[phase])
            elif guess in wronglet:
                print("You have already guessed that!")
                print(slots)
                print(stages[phase])
            else:
                print("Incorrect\n")
                incorrect(guess)
                phase += 1
                print(stages[phase])
                if phase == 7: 
                    loop = False
                    againloop = True
                    while againloop:
                        again = input("\nWant to try again? Please type yes or no: ")
                        if again == "yes":
                            assessGuesses()
                            againloop = False
                        elif again == "no":
                            print("Bye!")
                            againloop = False
                        else:
                            print("Please type yes or no. ") 
        else: 
            print("Please type in one letter")
        

def openspots(word):
    places = len(word)
    for slot in range(places):
        slots.append("_ ")
    print(slots)

def correct(word, index):
    slots[index] = word[index]
    print(slots)

def incorrect(letter):
    wronglet.append(letter)
    print(wronglet)
    print(slots)

def search(word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            return i
    return -1

assessGuesses()


# title for wrong letter list
# get rid of quotations and brackets
# display wrong letter list after guessing correct
