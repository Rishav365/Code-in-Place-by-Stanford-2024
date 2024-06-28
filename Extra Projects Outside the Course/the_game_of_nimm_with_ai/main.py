"""
Nimm Game

Author: Rishav Dey
Date: 16th May 2024
Version: 1.0

Description:
This program implements the game of Nimm, a turn-based game where players take turns removing 1, 2, or 3 stones from a pile. 
The game can be played against a friend or an AI opponent. Players can choose whether the winner is determined by the player 
who takes the last stone or the one who doesn't.

Libraries Used:
- random: Standard library for generating random numbers.

Usage:
Run the script and follow the prompts:
1. Choose to play against a friend or the AI.
2. Choose whether the winner is the player who takes the last stone or not.
3. Players take turns removing 1, 2, or 3 stones until no stones are left.
4. The winner is announced based on the chosen rule.

Notes:
- Ensure the program runs in an environment that supports user input.
- Clicking anywhere on the console will exit the program after completion.
"""

import random

def main():
    """Plays the game of Nimm with various options and enhancements."""
    # Ask user to choose opponent (friend or AI)
    opponent_type = choose_opponent()

    # Ask user to choose the winner rule (taking the last stone wins or loses)
    winner_by_last_stone = determine_winner_by_last_stone()

    stones_remaining = 20
    current_player = 1  # Player 1 starts

    while stones_remaining > 0:
        # Print current state
        print(f"\nThere are {stones_remaining} stones left.")

        # Player's turn
        if current_player == 1:
            print(f"Player {current_player}, would you like to remove 1, 2, or 3 stones? ", end='')
            stones_to_remove = get_valid_stone_count(1, 3, stones_remaining)
        else:
            # Opponent's turn (AI or Player 2)
            if opponent_type == "AI":
                stones_to_remove = intelligent_ai_choice(stones_remaining)
                print(f"AI Player removes {stones_to_remove} stones.")
            else:
                print(f"Player 2, would you like to remove 1, 2, or 3 stones? ", end='')
                stones_to_remove = get_valid_stone_count(1, 3, stones_remaining)

        # Update stones remaining and print a blank line for readability
        stones_remaining -= stones_to_remove
        print()

        # Check if the number of stones remaining is divisible by 3
        if stones_remaining > 0 and stones_remaining % 3 == 0:
            print(f"Since {stones_remaining} is divisible by 3, Player {current_player} must go again.")
        else:
            current_player = 2 if current_player == 1 else 1

    # Announce the winner based on the winning rule
    if winner_by_last_stone:
        winning_player = 2 if current_player == 1 else 1  # Last player to take a stone wins
    else:
        winning_player = current_player  # The other player wins

    print(f"Player {winning_player} wins!")

def choose_opponent():
    """Asks the user to choose between playing with a friend or the AI."""
    while True:
        choice = input("Do you want to play with a friend (f) or the AI (ai)? ").lower()
        if choice in ["f", "friend", "ai"]:
            return "friend" if choice in ["f", "friend"] else "AI"
        else:
            print("Invalid choice. Please enter 'f' for friend or 'ai' for AI.")

def get_valid_stone_count(min_value, max_value, stones_remaining):
    """Gets a valid number of stones to remove from user input."""
    while True:
        try:
            user_input = int(input())
            if min_value <= user_input <= max_value and user_input <= stones_remaining:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value} (and not more than the remaining stones): ")
        except ValueError:
            print("Invalid input. Please enter a number: ")

def determine_winner_by_last_stone():
    """Asks the user if the winner should be the player who takes the last stone."""
    while True:
        choice = input("Should the winner be the player who takes the last stone (y/n)? ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def intelligent_ai_choice(stones_remaining):
    """Intelligently decides the number of stones the AI should remove."""
    if stones_remaining > 3:
        return (stones_remaining - 1) % 4 or random.randint(1, 3)
    else:
        return stones_remaining

if __name__ == "__main__":
    main()
