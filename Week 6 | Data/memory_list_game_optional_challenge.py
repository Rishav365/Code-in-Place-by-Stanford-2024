"""
Memory List Game

Author: Rishav Dey
Date: 3rd June 2024
Version: 1.0

Description:
This Python program implements a memory game where players match pairs of numbers represented 
as cards in a list. It tests memory and logical thinking by challenging players to remember and 
find all pairs correctly. The game progresses with each turn revealing hidden values and updating the display based on user input.

Instructions:
1. The game starts by creating a list with pairs of numbers shuffled randomly.
2. Players guess indices to uncover and match pairs of numbers.
3. If two selected indices reveal matching numbers, those pairs are revealed.
4. If numbers do not match, the game indicates the mismatch and hides the numbers again.
5. The game continues until all pairs are correctly matched.
6. Players are prompted to press Enter to continue after each turn.
7. Upon completing the game, a victory message is displayed.

Libraries Used:
- random: for shuffling the list of numbers.

Usage:
Run the script and follow the on-screen instructions to play the Memory List Game.

"""
import random

NUM_PAIRS = 3

def main():
    """
    Main function to execute the memory game.
    """
    # Create truth list with pairs of numbers
    truth_list = create_truth_list(NUM_PAIRS)
    
    # Create displayed list with '*' to hide values initially
    displayed_list = create_displayed_list(len(truth_list))
    
    # Clear terminal screen
    clear_terminal()
    
    # Continue game until all pairs are matched
    while '*' in displayed_list:
        # Display current state of the game
        print(displayed_list)
        
        # Get valid index from the user for the first card
        index1 = get_valid_index(displayed_list)
        clear_terminal()
        print(displayed_list)
        
        # Get valid index from the user for the second card
        index2 = get_valid_index(displayed_list)
        clear_terminal()
        
        # Check if the values at the two indices match
        if truth_list[index1] == truth_list[index2]:
            print("Match!")
            # Reveal the matched pairs
            displayed_list[index1] = truth_list[index1]
            displayed_list[index2] = truth_list[index2]
        else:
            print(f"No match. {truth_list[index1]} does not match {truth_list[index2]}.")
        
        # Wait for user to press Enter to continue
        input("Press Enter to continue...")
        clear_terminal()
    
    # Display victory message
    print("Congratulations! You won!")

def create_truth_list(num_pairs):
    """
    Creates a list with values 0 through num_pairs-1 twice.
    """
    truth_list = []
    for i in range(num_pairs):
        truth_list.append(i)
        truth_list.append(i)
    return truth_list

def create_displayed_list(length):
    """
    Creates a list with '*' to hide values initially.
    """
    displayed_list = ['*' for _ in range(length)]
    return displayed_list

def get_valid_index(displayed_list):
    """
    Gets a valid index from the user.
    """
    while True:
        try:
            index = int(input("Enter an index: "))
            if index < 0 or index >= len(displayed_list):
                print("Index out of range. Try again.")
            elif displayed_list[index] != '*':
                print("This number has already been matched. Try again.")
            else:
                return index
        except ValueError:
            print("Not a number. Try again.")

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()