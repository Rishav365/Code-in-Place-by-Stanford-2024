"""
The Game of Nimm

Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate 
taking stones until there are zero left. 

The game of Nimm goes as follows:

- The game starts with a pile of 20 stones between the players
- The two players alternate turns
- On a given turn, a player may take either 1 or 2 stone from the center pile
- The two players continue until the center pile has run out of stones.

The last player to take a stone loses.

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

        # Update stones remaining and switch player
        stones_remaining -= stones_to_remove
        print()  # Empty line for readability

        # Check if the number of stones remaining is divisible by 3
        if stones_remaining > 0 and stones_remaining % 3 == 0:
            print(f"Since {stones_remaining} is divisible by 3, Player {current_player} must go again.")
        else:
            current_player = 2 if current_player == 1 else 1

    # Announce the winner based on who takes the last stone
    winning_player = current_player  # Last player to take a stone

    if winner_by_last_stone:
        print(f"Player {winning_player} wins!")
    else:
        print(f"Player {(winning_player % 2) + 1} wins! (Player who didn't take the last stone)")

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
                print(f"Please enter a number between {min_value} and {min_value} (and not more than the remaining stones): ")
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
    if stones_remaining % 4 == 0:
        return random.randint(1, 3)
    else:
        return stones_remaining % 4

if __name__ == "__main__":
    main()
