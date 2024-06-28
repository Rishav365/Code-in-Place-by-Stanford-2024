"""
Khansole Academy

A program that helps other people learn addition! 
This program randomly generates a simple addition problem for 
the user, reads in the answer from the user, and then checks to see if they got it right or wrong.

"""
import random

def main():
    # Print the title of the program
    print("Khansole Academy")
    
    # Variable to keep track of the number of correct answers in a row
    correct_in_a_row = 0
    
    # Continue asking questions until the user gets 3 correct in a row
    while correct_in_a_row < 3:
        # Generate two random numbers between 10 and 99
        random_num1 = random.randint(10, 99)
        random_num2 = random.randint(10, 99)
        
        # Calculate the correct answer
        correct_answer = random_num1 + random_num2
        
        # Ask the user the addition question
        print(f"What is {random_num1} + {random_num2}?")
        
        # Get the user's answer
        user_answer = int(input("Your answer: "))
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            # Increment the count of correct answers in a row
            correct_in_a_row += 1
            print("Correct!")
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            # Reset the count of correct answers in a row to 0
            correct_in_a_row = 0
            print("Incorrect.")
            print(f"The expected answer is {correct_answer}")
    
    # Print a congratulatory message when the user gets 3 correct in a row
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
