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
stages = ["", "________", "|  |", "|  | ", "|  0 ", "| /|\ ", "| / \ ", "| "]
for stage in stages:
    print(f"{stage}")
phase = 0

# List of Words, blank spots and the wrong letters
words = "l i o n,t i g e r,g o a t,h o r s e,d o n k e y,d o g,c a t,p i g".split(",")
slots = []
wronglet = []

# FUNCTIONS
def getWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex].split(" ")

def assessGuesses():
    word = getWord(words)
    print(word)
    openspots(word)
    loop = True
    while loop:
        guess = input("Pick a letter: ")
        if guess in slots: 
            print("You have already guessed that!")
            print(slots)
        elif guess in word:
            print("present")
            gueIndex = search(word, guess)
            correct(word, gueIndex)
        elif guess in wronglet:
            print("You have already guessed that!")
            print(slots)
        else:
            print("not present")
            incorrect(guess)


def openspots(word):
    places = len(word)
    for slot in range(places):
        slots.append("_ ")
    print(slots)

def correct(word, index):
    print("correct function")
    slots[index] = word[index]
    print(slots)

def incorrect(letter):
    print("incorrect function")
    wronglet.append(letter)
    print(wronglet)
    print(slots)
    print(stages[phase + 1])

def search(word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            return i
    return -1

# def nextstage():
#     for stage in range(len(stages)):
#         stage += 1
#         return stages[stage]



assessGuesses()