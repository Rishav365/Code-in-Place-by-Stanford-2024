"""
Heads Up! Word Guessing Game

Author: Rishav Dey
Date: 31st May 2024
Version: 1.0

Description:
This Python script implements a word guessing game inspired by "Heads Up!". 
The game randomly selects words from a file ('cswords.txt') and displays them one at a time. 
Players try to guess the word based on hints provided by others. 
This version allows for remote play, where players can take turns displaying words to others via video call or chat, and friends can participate by guessing the word.

How to Play:
- The game starts with a welcome message and loads words from the file.
- A word is randomly chosen and displayed to the player.
- Players take turns providing hints or descriptions of the word to others remotely.
- Remote players try to guess the word based on the hints provided.
- After each word, press Enter to show the next word.
- The game continues until all words from the file have been displayed.
"""

import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines


def main():
    print("Welcome to Heads Up!")
    
    # Get words from the file.
    words = get_words_from_file()
    
    # Show a randomly chosen word.
    while True:
        random_word = random.choice(words)
        print("\nNext word: ", random_word)
        
        # Wait for user to hit enter.
        input("Press Enter to show another word...")
    
if __name__ == '__main__':
    main()