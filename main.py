# HANGMAN PROJECT BY SANA

import random

# create an array filled with words and their letters 
# could be a dictionary for each letter, open slots, and words
# pick a random word
# ask for a letter
# test if the letter is in the word
# correct letter means add to open slot
# wrong letter means add a stage 
# dictionary of all letters, if letter is chosen, letter will appear in dictionary

# Hangman Appearance
stages = ["", "________", "________\n|  |", "________\n|  |\n|  | ", "________\n|  |\n|  | \n|  0 ", "________\n|  |\n|  | \n|  0 \n| /|\ ", "________\n|  |\n|  | \n|  0 \n| /|\ \n| / \ ", "________\n|  |\n|  | \n|  0 \n| /|\ \n| / \ \n| \nYOU LOST!"]
# for stage in stages:
#     print(f"{stage}")



# List of Words, blank spots and the wrong letters
words = "l i o n,t i g e r,g o a t,h o r s e,d o n k e y,d o g,c a t,p i g".split(",")
slots = []
wronglet = []

# FUNCTIONS
def getWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex].split(" ")

def assessGuesses():
    slots.clear()
    wronglet.clear()
    phase = 0
    word = getWord(words)
    print(word)
    openspots(word)
    loop = True
    while loop:
        guess = input("\nPick a letter: ")
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
                again = input("\nWant to try again? Please type yes or no: ")
                if again == "yes":
                    assessGuesses()
                elif again == "no":
                    print("Bye!")
                else:
                    print("Please type yes or no. ")
                    again = input("Want to try again? Please type yes or no: ")

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


