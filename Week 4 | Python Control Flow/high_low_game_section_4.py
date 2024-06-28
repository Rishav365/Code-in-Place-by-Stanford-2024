"""
High-Low Number Guessing Game

Author: Rishav Dey
Date: 12th May 2024
Version: 1.0

Description:

This Python script implements a high-low number guessing game. 
The game consists of multiple rounds where the player guesses whether 
their randomly generated number is higher or lower than the computer's 
randomly generated number. The player earns points based on correct guesses 
and receives feedback after each round. At the end of all rounds, the final 
score is displayed along with a message based on the performance.

"""

import random

NUM_ROUNDS = 5 

def main():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    score = 0  # Initializing score to keep track across rounds.

    # Loop for the number of rounds.
    for round_num in range(1, NUM_ROUNDS + 1):
        # Call the play function for each round and update the score.
        score = play(round_num, score)
        # Separate rounds visually.
        print()

    # Print the final message based on the score.
    if score == NUM_ROUNDS:
        print(f"Wow! You played perfectly!\n\nThanks for Playing!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!\n\nThanks for Playing!")
    else:
        print(f"Better luck next time!\n\nThanks for Playing!")

def play(round_num, score):
    # Generate random numbers for the user and computer.
    num_user = random.randint(1, 100)
    num_computer = random.randint(1, 100)

    # Display round number and user's number.
    print(f"Round {round_num} \nYour number is {num_user}")

    # Get user's guess and convert to lowercase for case-insensitive comparison.
    user_answer = input("Do you think your number is higher or lower than the computer's?: ").lower()

    # Validate user's input.
    while user_answer not in ["higher", "lower"]:
        user_answer = input("Please enter either 'higher' or 'lower': ").lower()
    
    # Check if user's guess is correct and update score accordingly.
    if user_answer == "lower":
        if num_user < num_computer:
            print(f"You were right! The computer's number was {num_computer}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {num_computer}")
    elif user_answer == "higher":
        if num_user > num_computer:
            print(f"You were right! The computer's number was {num_computer}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {num_computer}")

    # Display current score.
    print(f"Your score is now {score}")
    return score  # Returns the updated score.

if __name__ == "__main__":
    main()
