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

words = "l i o n,t i g e r,g o a t,h o r s e,d o n k e y,d o g,c a t,p i g".split(",")

def getWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex].split(" ")

def assessGuesses():
    word = getWord(words)
    print(word)
    openspots(word)
    guess = input("Pick a letter: ")
    if guess in word:
        print("present")
    else:
        print("not present")

def openspots(word):
    slots = []
    places = len(word)
    for slot in range(places):
        slots.append("_ ")
    print(slots)
assessGuesses()