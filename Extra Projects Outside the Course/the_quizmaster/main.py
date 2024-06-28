"""
The QuizMaster

**Author**: Rishav Dey  
**Date**: 16th June 2024  
**Version**: 1.0  

**Description**:  

This quiz program takes you through 8 rounds of increasingly challenging general knowledge questions. 
Each round features 5 questions, and the time limit for each question increases as the difficulty level rises. 
Test your knowledge, race against the clock, and see how many questions you can get right!


**Libraries Used**:
- `random`: Standard library for generating random numbers.
- `time`: Standard library for time-related functions.
- `signal`: Standard library for handling timeouts.

**Usage**:
Run the script and follow the prompts:
1. Confirm if you are ready to start the quiz.
2. Each round consists of 5 questions with increasing difficulty.
3. Answer each question within the given time limit.
4. After each round, you will receive feedback and be asked if you want to continue to the next round.
5. The quiz continues until all 8 rounds are completed or you choose to stop.

**Notes**:
- Ensure the program runs in an environment that supports user input.
- The program will take no input as a skip for the question.

**Example**:
1. Start the quiz by confirming you are ready.
2. For each round, answer the questions within the time limit.
3. Receive feedback on your performance after each round.
4. Continue to the next round or choose to end the quiz at any time.
5. At the end, see your total correct answers and receive a final message.

**Additional Information**:
- The program uses the `signal` library to enforce time limits on each question.
- Feedback is provided after each round to encourage and inform the player.

Enjoy challenging yourself with QuizMaster!

"""

import random
import time
import signal
from questions import quiz_questions

# Exception for handling timeouts
class TimeoutException(Exception):
    pass

# Handler for timeout
def timeout_handler(signum, frame):
    raise TimeoutException("Timeout expired.")

# Ensure that the user input is one of the valid options.
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print("Invalid input. Please enter one of the following: ", "/".join(valid_options))

def quizmaster():
    # Display welcome messages
    print("Welcome to the QuizMaster!")
    time.sleep(0.8)
    print("The Ultimate General Knowledge Quiz!")
    time.sleep(1.5)
    print("This quiz has 8 rounds with 5 questions in each round.")
    time.sleep(0.8)
    print("The difficulty level will increase with each round.")
    time.sleep(0.8)
    print("Each question will be timed. The given time will increase with difficulty to be fair.")
    time.sleep(0.8)
    print(f"If you enter nothing, the program will take it as a skip.\n")
    time.sleep(0.8)

    while True:
        # Confirm if the user is ready to start the quiz
        ready_to_start = get_valid_input("Are you ready to dive in? (yes/no): ", ["yes", "no"])
        if ready_to_start != 'yes':
            print(f"Come back when you're ready. Goodbye!\n")
            time.sleep(1)
            return

        # Dot animation for starting the quiz
        print("Let's begin!\n")
        time.sleep(0.9)
        print("Starting the quiz", end="")
        for _ in range(4):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        num_rounds = 8
        questions_per_round = 5
        correct_count = 0
        total_count = 0
        asked_questions = set()

        # Loop through each round
        for round_num in range(1, num_rounds + 1):
            time.sleep(0.9)
            print(f"\nRound {round_num}")
            time.sleep(0.9)
            question_time_limit = 12 + (round_num - 1) * 2
            print(f"You will have {question_time_limit} seconds for this round.")
            time.sleep(0.9)
            print("I hope you are ready…")
            time.sleep(1)
            print("The next round is starting in…")

            # Countdown before starting the round
            for countdown in range(3, 0, -1):
                print(countdown)
                time.sleep(1)
            print(f"Go!\n")

            # Play the round and collect results
            round_correct_count, round_time_taken = play_round(round_num, questions_per_round, asked_questions, question_time_limit)
            correct_count += round_correct_count
            total_count += questions_per_round

            # Encouragement message after each round
            print(f"\nYou got {round_correct_count}/{questions_per_round} questions correct in this round.")
            time.sleep(0.8)
            print(f"Total time taken for this round: {round_time_taken:.2f} seconds.")
            time.sleep(0.8)
            if round_correct_count == questions_per_round:
                print("Fantastic! You got all the questions right!")
            elif round_correct_count >= questions_per_round * 0.8:
                print("Great job! You're doing excellent!")
            elif round_correct_count >= questions_per_round * 0.6:
                print("Good effort! Keep going!")
            else:
                print("Keep trying! You'll get better!")

            time.sleep(1)

            # Additional encouragement for increasing rounds
            if round_num < num_rounds:
                print(f"You're doing great! Keep it up for round {round_num + 1}!\n")
                time.sleep(1)

                # Check if the user wants to continue to the next round
                continue_playing = get_valid_input("Do you want to continue to the next round? (yes/no): ", ["yes", "no"])
                if continue_playing != 'yes':
                    break

        # Special message after the final round
        if round_num == num_rounds:
            print("\nCongratulations on making it this far!")
            time.sleep(1)

        # Print the final score and encouragement message
        print(f"\nYou got {correct_count}/{total_count} questions correct overall.")
        time.sleep(1)
        if correct_count == total_count:
            print(f"Congratulations! You aced the quiz!\n")
        elif correct_count >= total_count * 0.8:
            print(f"Well done! You have an excellent general knowledge!\n")
        elif correct_count >= total_count * 0.6:
            print(f"Good job! Keep learning and improving your knowledge.\n")
        else:
            print(f"Better luck next time! Keep practicing to improve your general knowledge.\n")
        time.sleep(2)

        # Ask if the user wants to play again
        play_again = get_valid_input("Do you want to play the QuizMaster again? (yes/no): ", ["yes", "no"])
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!\n")
            break


def play_round(round_num, questions_per_round, asked_questions, question_time_limit):
    correct_count = 0
    available_questions = []

    # Collect available questions for this round
    for question, (answer, difficulty) in quiz_questions.items():
        if question not in asked_questions and difficulty <= round_num:
            available_questions.append((question, answer, difficulty))

    # Ensure we don't sample more questions than available
    questions_per_round = min(questions_per_round, len(available_questions))
    round_questions = random.sample(available_questions, questions_per_round)
    total_time_taken = 0

    # Loop through each question in the round
    for i, (question, answer, difficulty) in enumerate(round_questions):
        asked_questions.add(question)
        print(f"Question {i + 1}: {question}")
        time.sleep(0.5)

        start_time = time.time()

        # Set up the alarm signal for timeout
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(question_time_limit)

        try:
            print(f"You have {question_time_limit - int(time.time() - start_time)} seconds left...")
            user_answer = input(f"Answer: ").strip().lower()
        except TimeoutException:
            user_answer = ''

        # Disable the alarm after input received or timeout
        signal.alarm(0)
        elapsed_time = time.time() - start_time
        total_time_taken += elapsed_time

        # Evaluate user's answer
        if not user_answer:
            print("You entered nothing, so it will be taken as a skip.")
            time.sleep(1)
            print(f"The answer is {answer}.\n")
            time.sleep(2)
        elif user_answer == answer.lower():
            if elapsed_time >= question_time_limit:
                print(f"That is correct, but your answer won't count as you didn't answer within the time limit.\n")
                time.sleep(3)
            else:
                print(f"That is correct! It is indeed {answer}.\n")
                correct_count += 1
        else:
            print(f"That is incorrect, the correct answer is {answer}.\n")
            time.sleep(1)

    return correct_count, total_time_taken



if __name__ == "__main__":
    quizmaster()