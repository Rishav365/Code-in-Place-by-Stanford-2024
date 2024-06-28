"""
Atlas: The Capital Guessing Game

Author: Rishav Dey
Date: 28th June 2024
Version: 1.0

Description:
This program is a game called Atlas, where players guess the capitals of countries. 
The game consists of multiple rounds, each with a set number of questions. Players 
have a limited time to answer each question, and their performance is scored and 
feedback is provided after each round. The game can be played in multiple rounds, 
and players can choose to continue or exit after each round.

How to Play:
1. The game will prompt you to start.
2. You will have a set time to answer each question.
3. If you don't answer in time or enter nothing, it will be considered a skip.
4. Your score and feedback will be provided after each round.
5. You can choose to continue to the next round or exit the game.

Libraries Required:
- random
- time
- signal
- atlas_questions: A module containing a list of country-capital pairs.

Usage:
Run the script and follow the on-screen instructions.

"""
import random
import time
import signal
from atlas_questions import atlas_questions

# Exception for handling timeouts
class TimeoutException(Exception):
    pass

# Handler for timeout
def timeout_handler(signum, frame):
    raise TimeoutException("Timeout expired.")


def atlas():
    # The main function for the game.
    num_rounds = 8
    questions_per_round = 5
    question_time_limit = 10  # Set the time limit for each question

    # Function to get a random set of questions for a given round
    def get_round_questions(num_questions):
        return random.sample(atlas_questions, num_questions)

    # Initialize the game
    print("Welcome to Atlas! Guess the capital of the following countries.")
    time.sleep(0.8)
    print(f"This game has {num_rounds} rounds with {questions_per_round} questions in each round.")
    time.sleep(0.8)
    print("Each question will be timed, and you'll have 10 seconds to answer.")
    time.sleep(0.8)
    print("If you don't answer in time or enter nothing, it will be taken as a skip.\n")
    time.sleep(0.8)

    total_score = 0
    total_questions_attempted = 0  # Track total questions attempted across rounds
    asked_countries = []

    while True:
        round_num = 0  # Track current round number
        total_time_taken = 0

        ready_to_start = input("Are you ready to guess some capitals? (yes/no): ").strip().lower()
        if ready_to_start != 'yes':
            print("Come back when you're ready. Goodbye!")
            time.sleep(1)
            break

        print("Okay, here you go...")
        time.sleep(0.9)
        print("Starting in", end="")
        for _ in range(4):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("")
        for countdown in range(3, 0, -1):
            print(countdown)
            time.sleep(1)
        print(f"Go!\n")

        while round_num < num_rounds:
            round_num += 1
            score = 0
            round_time_taken = 0

            print(f"\nRound {round_num}")
            time.sleep(0.9)
            print(f"You will have {question_time_limit} seconds for each question.")
            time.sleep(0.9)
            print("I hope you are ready…")
            time.sleep(1)
            print("The next round is starting in…")
            for countdown in range(3, 0, -1):
                print(countdown)
                time.sleep(1)
            print(f"Go!\n")

            round_questions = get_round_questions(questions_per_round)

            for question_num, q in enumerate(round_questions, 1):
                country = q["country"]
                capital = q["capital"]
                asked_countries.append(country)

                print(f"Question {question_num}: What is the capital of {country}?")
                time.sleep(0.5)

                start_time = time.time()
                user_input = input("Your answer: ").strip()
                elapsed_time = time.time() - start_time

                round_time_taken += elapsed_time

                print()

                if not user_input:
                    print("Time's up or you entered nothing! The answer is taken as a skip.")
                    time.sleep(1)
                elif user_input.lower() == capital.lower():
                    if elapsed_time >= question_time_limit:
                        print(f"That is correct, but your answer won't count as you didn't answer within the time limit.\n")
                        time.sleep(3)
                    else:
                        print("Correct!")
                        score += 1
                else:
                    print(f"Sorry, the capital of {country} is {capital}.")

                print()
                time.sleep(1)

            total_questions_attempted += question_num
            total_score += score
            total_time_taken += round_time_taken

            print(f"\nYou got {score}/{questions_per_round} questions correct in this round.")
            print(f"Total time taken for this round: {round_time_taken:.2f} seconds.")
            time.sleep(0.8)

            # Provide feedback based on the score
            if score == questions_per_round:
                print("Fantastic! You got all the questions right!")
            elif score >= questions_per_round * 0.8:
                print("Great job! You're doing excellent!")
            elif score >= questions_per_round * 0.6:
                print("Good effort! Keep going!")
            else:
                print("Keep trying! You'll get better!")

            time.sleep(1)

            continue_playing = input("Do you want to continue to the next round? (yes/no): ").strip().lower()
            if continue_playing != 'yes':
                break

        # Display final score and feedback
        print(f"\nYour final score is: {total_score}/{total_questions_attempted}")
        print(f"Total time taken: {total_time_taken:.2f} seconds.")
        time.sleep(1)
        if total_score == total_questions_attempted:
            print("Congratulations! You aced the quiz!")
        elif total_score >= total_questions_attempted * 0.8:
            print("Well done! You have excellent knowledge of world capitals!")
        elif total_score >= total_questions_attempted * 0.6:
            print("Good job! Keep learning and improving your skills.")
        else:
            print("Better luck next time! Keep practicing to improve your knowledge of world capitals.")

        print(f"Thanks for playing Atlas!\n")
        time.sleep(2)
        break

    time.sleep(1)

if __name__ == "__main__":
    atlas()