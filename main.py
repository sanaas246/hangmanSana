# HANGMAN PROJECT BY SANA

import random

# Hangman Appearance
stages = ["", "________", "________\n|  |", "________\n|  |\n|  | ", "________\n|  |\n|  | \n|  0 ", "________\n|  |\n|  | \n|  0 \n| /|\ ", "________\n|  |\n|  | \n|  0 \n| /|\ \n| / \ ", "________\n|  |\n|  | \n|  0 \n| /|\ \n| / \ \n| \nYOU LOST!"]

# List of Words, blank spots and the wrong letters
words = "l i o n,t i g e r,g o a t,h o r s e,d o n k e y,d o g,c a t,p i g, g o r i l l a, c h i m p a n z e e , m o n k e y, b e a v e r, o r a n g u t a n, a n t e l o p e, b a t".split(",")

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
    print("\nHANGMAN")
    openspots(word)
    # loop to continue guessing
    loop = True
    while loop:
        guess = input("\nPick a letter: ").lower()
        # if the user input is one lowercase letter then...
        if guess.isalpha() and len(guess) == 1:
            # if the user input has been used already
            if guess in slots: 
                print("\nYou have already guessed that!\n")
                spots = ' '.join(slots)
                print(spots)
                print(stages[phase])
            # if the user input is in the word's string
            elif guess in word:
                print("Correct\n")
                search(word, guess)
                wrong = ' '.join(wronglet)
                print("Wrong letters: ", wrong)
                print(stages[phase])
                # if the entire word is guessed
                if slots == word:
                    loop = False
                    print("\nGood Job! You win!")
                    playagain()
            # if the guess has been used already
            elif guess in wronglet:
                print("\nYou have already guessed that!\n")
                spots = ' '.join(slots)
                print(spots)
                print(stages[phase])
            # if the user selects the wrong letters
            else:
                print("Incorrect\n")
                incorrect(guess)
                phase += 1
                print(stages[phase])
                if phase == 7: 
                    loop = False
                    playagain()      
        else: 
            print("Please type in one letter")

def playagain():
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

def openspots(word):
    places = len(word)
    for slot in range(places):
        slots.append("_ ")
    spots = ' '.join(slots)
    print(spots)  

def incorrect(letter):
    wronglet.append(letter)
    wrong = ' '.join(wronglet)
    print("Wrong letters: ", wrong, "\n")
    spots = ' '.join(slots)
    print(spots)

def search(word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            slots[i] = word[i]
            spots = ' '.join(slots)
    print(spots, "\n")
    return -1

assessGuesses()

