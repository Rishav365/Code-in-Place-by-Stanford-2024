import random
import time
import signal
from fractions import Fraction
from questions import quiz_questions
from atlas_questions import atlas_questions

# Exception for handling timeouts
class TimeoutException(Exception):
    pass

# Handler for timeout
def timeout_handler(signum, frame):
    raise TimeoutException("Timeout expired.")

# Global constants for planetary weight calculator
MERCURY = 0.376
VENUS = 0.889
MARS = 0.378
JUPITER = 2.360
SATURN = 1.081
URANUS = 0.815
NEPTUNE = 1.14
EARTH = 1.0

# Global constants for cat and dog years conversion
CAT_YRS_MULTIPLIER = 4
DOG_YRS_MULTIPLIER = 7.18

# Affirmation function
AFFIRMATION = "I am capable of doing anything I put my mind to."

def wholesome_machine():
    # Prompt user to type affirmation
    print("Please type the following affirmation: " + AFFIRMATION)
    time.sleep(1)
    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        print("That was not the affirmation.")
        time.sleep(1)
        print("Please type the following affirmation: " + AFFIRMATION)
        time.sleep(1)
        user_feedback = input()
    print("That's right! :)")
    time.sleep(1)

##########################################################################
"""The QuizMaster"""

"""This quiz program takes you through 8 rounds of increasingly challenging general knowledge questions. 
Each round features 5 questions, and the time limit for each question increases as the difficulty level rises. 
Test your knowledge, race against the clock, and see how many questions you can get right!"""

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

    # Confirm if the user is ready to start the quiz
    ready_to_start = input("Are you ready to dive in? (yes/no): ").strip().lower()
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
        # Check if the user wants to continue to the next round
        continue_playing = input("Do you want to continue to the next round? (yes/no): ").strip().lower()
        if continue_playing != 'yes':
            break

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

##########################################################################
"""Atlas: The Capital Guessing Game"""

def atlas():
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

##########################################################################
"""The Math Practice Program"""

"""
This program provides a comprehensive math tutoring experience, allowing users
to practice various categories of math problems (Addition, Subtraction, 
Multiplication, Division, and Algebra) at different difficulty levels (Easy, 
Medium, Hard). Each session consists of timed quizzes, where users can input 
answers in fractional form or as rounded decimals. The program tracks scores, 
provides feedback based on performance, and offers continuous rounds of 
practice until the user decides to stop. Enjoy improving your math skills with 
this interactive and educational tool!

"""
def math_practice():
    
# Function to display welcome messages
    def welcome_message():
        print("Welcome to the Math Practice Program!")
        time.sleep(0.8)
        print("You can choose from various categories of math problems.")
        time.sleep(0.8)
        print("Each category has multiple levels of difficulty.")
        time.sleep(0.8)
        print("You will be timed for each question, so try to answer as quickly as possible!")
        time.sleep(0.8)
        print("You can provide your answers in fractional form or as a decimal rounded to 2 or 3 significant figures.\n")
        time.sleep(1.5)
        print("If you want to skip a question, simply leave the answer blank.")
        time.sleep(0.8)
        print("Let's get started!\n")
        time.sleep(1)

    # Function to choose a math category
    def choose_category():
        categories = {
            '1': 'Addition',
            '2': 'Subtraction',
            '3': 'Multiplication',
            '4': 'Division',
            '5': 'Algebra'
        }
        print("Choose a category:")
        for key, value in categories.items():
            print(f"{key}. {value}")
        while True:
            choice = input("Enter the number of your choice: ").strip()
            if choice in categories:
                return categories[choice]
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)

    # Function to choose difficulty level
    def choose_difficulty():
        difficulties = {
            '1': 'Easy',
            '2': 'Medium',
            '3': 'Hard'
        }
        print("Choose a difficulty level:")
        for key, value in difficulties.items():
            print(f"{key}. {value}")
        while True:
            choice = input("Enter the number of your choice: ").strip()
            if choice in difficulties:
                return difficulties[choice]
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)

    # Function to generate a specific type of math question based on category and difficulty
    def generate_question(category, difficulty):
        if category == 'Addition':
            return generate_addition_question(difficulty)
        elif category == 'Subtraction':
            return generate_subtraction_question(difficulty)
        elif category == 'Multiplication':
            return generate_multiplication_question(difficulty)
        elif category == 'Division':
            return generate_division_question(difficulty)
        elif category == 'Algebra':
            return generate_algebra_question(difficulty)

    # Functions to generate random numbers for different operations based on difficulty level
    def generate_random_number_addition(difficulty):
        if difficulty == 'Easy':
            return random.randint(-100, 100)
        elif difficulty == 'Medium':
            return round(random.uniform(-500, 500), 2)
        elif difficulty == 'Hard':
            return Fraction(random.randint(-1000, 1000), random.randint(10, 1000))

    def generate_random_number_subtraction(difficulty):
        if difficulty == 'Easy':
            return random.randint(-20, 20)
        elif difficulty == 'Medium':
            return round(random.uniform(-50, 50), 2)
        elif difficulty == 'Hard':
            return Fraction(random.randint(-1000, 1000), random.randint(100, 1000))

    def generate_random_number_multiplication(difficulty):
        if difficulty == 'Easy':
            return random.randint(-10, 10)
        elif difficulty == 'Medium':
            return round(random.uniform(-50, 50), 2)
        elif difficulty == 'Hard':
            return Fraction(random.randint(-100, 100), random.randint(-100, 100))

    def generate_random_number_division(difficulty):
        if difficulty == 'Easy':
            numerator = random.randint(1, 10)
            denominator = random.randint(1, 10)
            return Fraction(numerator, denominator)
        elif difficulty == 'Medium':
            numerator = random.randint(10, 50)
            denominator = random.randint(2, 10)
            return Fraction(numerator, denominator)
        elif difficulty == 'Hard':
            numerator = random.randint(50, 100)
            denominator = random.randint(2, 20)
            return Fraction(numerator, denominator)

    # Functions to generate specific types of math questions based on difficulty level
    def generate_addition_question(difficulty):
        a, b = generate_random_number_addition(difficulty), generate_random_number_addition(difficulty)
        return f"{a} + {b}", a + b

    def generate_subtraction_question(difficulty):
        a, b = generate_random_number_subtraction(difficulty), generate_random_number_subtraction(difficulty)
        return f"{a} - {b}", a - b

    def generate_multiplication_question(difficulty):
        a, b = generate_random_number_multiplication(difficulty), generate_random_number_multiplication(difficulty)
        return f"{a} * {b}", a * b

    def generate_division_question(difficulty):
        a = generate_random_number_division(difficulty)
        b = generate_random_number_division(difficulty)
        while b == 0:
            b = generate_random_number_division(difficulty)
        a = a * b
        return f"{a} / {b}", Fraction(a, b)

    def generate_algebra_question(difficulty):
        if difficulty == 'Easy':
            a, b = random.randint(1, 10), random.randint(1, 10)
            return f"x + {a} = {a + b}", b
        elif difficulty == 'Medium':
            a, b = Fraction(random.randint(-10, 10), random.randint(1, 10)), random.randint(1, 20)
            return f"{a}x = {float(a * b)}", b
        elif difficulty == 'Hard':
            a, b, c = Fraction(random.randint(-10, 10), random.randint(1, 10)), random.randint(-20, 20), random.randint(-20, 20)
            return f"{a}x + {b} = {c}", Fraction(c - b, a)

    # Function to get user input with a timeout
    def input_with_timeout(prompt, timeout):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        try:
            return input(prompt)
        except TimeoutException:
            return None
        finally:
            signal.alarm(0)

    # Function to check if user's answer matches the correct answer
    def check_answer(user_answer, correct_answer, tolerance=1e-3):
        try:
            if abs(float(user_answer) - float(correct_answer)) < tolerance:
                return True
        except ValueError:
            pass

        try:
            if Fraction(user_answer) == Fraction(correct_answer):
                return True
        except ValueError:
            pass

        return False

    # Main function to run the math tutor program
    def main_math():
        welcome_message()
        total_score = 0
        total_questions = 0
        asked_questions = set()
        question_number = 1

        while True:
            category = choose_category()
            difficulty = choose_difficulty()
            question_count = 5
            correct_count = 0
            skipped_count = 0
            round_time_taken = 0

            print(f"\nStarting {category} questions at {difficulty} level.")
            time.sleep(0.9)
            time_limit = 15 + (difficulty == 'Medium') * 10 + (difficulty == 'Hard') * 15
            print(f"You will have {time_limit} seconds for each question.")
            time.sleep(0.9)
            print("I hope you are ready...")
            time.sleep(0.9)
            print("The next round is starting in...")
            for countdown in range(3, 0, -1):
                print(countdown)
                time.sleep(0.9)
            print("Go!")

            for _ in range(question_count):
                question, answer = generate_question(category, difficulty)
                while question in asked_questions:
                    question, answer = generate_question(category, difficulty)
                asked_questions.add(question)

                print(f"\nQuestion {question_number}: {question}")
                start_time = time.time()
                user_answer = input_with_timeout(f"Answer (you have {time_limit} seconds left): ", time_limit)
                elapsed_time = time.time() - start_time
                round_time_taken += elapsed_time
                question_number += 1

                if user_answer is None:
                    print("Oops, time's up...on to the next question...")
                    time.sleep(0.55)
                    print(f"The correct answer is {answer}.\n")
                elif not user_answer.strip():
                    print("You skipped this question.\n")
                    skipped_count += 1
                elif check_answer(user_answer.strip(), answer):
                    if elapsed_time >= time_limit:
                        print(f"That is correct, but your answer won't count as you didn't answer within the time limit.\n")
                    else:
                        print(f"That is correct! Answer: {answer}.\n")
                        correct_count += 1
                else:
                    print(f"That is incorrect, the correct answer is {answer}.\n")

            total_score += correct_count
            total_questions += question_count - skipped_count

            print(f"\nYou got {correct_count}/{question_count - skipped_count} questions correct in this round.")
            time.sleep(0.5)
            print(f"You skipped {skipped_count} questions.")
            time.sleep(0.5)
            print(f"Total time taken for this round: {round_time_taken:.2f} seconds.")
            time.sleep(0.5)
            if correct_count == question_count - skipped_count:
                print("Fantastic! You got all the questions right!")
            elif correct_count >= (question_count - skipped_count) * 0.8:
                print("Great job! You're doing excellent!")
            elif correct_count >= (question_count - skipped_count) * 0.6:
                print("Good effort! Keep going!")
            else:
                print("Keep trying! You'll get better!")

            time.sleep(1)
            continue_playing = input("Do you want to continue practicing? (yes/no): ").strip().lower()
            if continue_playing != 'yes':
                break

        print(f"\nYou got {total_score}/{total_questions} questions correct overall.")
        time.sleep(1)
        if total_score == total_questions:
            print("Congratulations! You aced the quiz!")
        elif total_score >= total_questions * 0.8:
            print("Well done! You have excellent math skills!")
        elif total_score >= total_questions * 0.6:
            print("Good job! Keep learning and improving your skills.")
        else:
            print("Better luck next time! Keep practicing to improve your math skills.")
        time.sleep(2)

    # Entry point to start the main math tutor program
    main_math()

##########################################################################

"""The Game Of Nimm"""

def game_of_nimm():
    # Plays the game of Nimm with various options and enhancements.
    rounds = 5
    scores = {"Player 1": 0, "Player 2": 0, "AI": 0}

    print("Welcome to the Game of Nimm!")
    time.sleep(0.9)
    print("In this game, you will take turns with your opponent to remove 1, 2, or 3 stones from a pile.")
    time.sleep(0.9)
    print("This game has 5 rounds.")
    time.sleep(0.9)
    print("The winner is determined based on whether taking the last stone wins or loses, which you can set at the beginning.")
    time.sleep(0.9)
    print()

    while True:  # Loop to play the game again if user chooses
        opponent_type = choose_opponent()
        winner_by_last_stone = determine_winner_by_last_stone()
        total_stones = select_total_stones()

        ready_to_start = input("Are you ready to start playing? (yes/no): ").strip().lower()
        if ready_to_start not in ['yes', 'y']:
            print("Exiting the game of Nimm...")
            time.sleep(0.9)
            print("Goodbye!")
            time.sleep(0.9)
            break

        for round_number in range(1, rounds + 1):
            print(f"\nStarting Round {round_number} of {rounds}!")
            stones_remaining = total_stones
            current_player = 1  # Player 1 starts

            while stones_remaining > 0:
                print(f"\nThere are {stones_remaining} stones left.")
                time.sleep(1)  # Pause for readability

                if current_player == 1:
                    print(f"Player {current_player}, would you like to remove 1, 2, or 3 stones? ", end='')
                    stones_to_remove = get_valid_stone_count(1, 3, stones_remaining)
                else:
                    if opponent_type == "AI":
                        stones_to_remove = intelligent_ai_choice(stones_remaining)
                        print(f"AI Player removes {stones_to_remove} stones.")
                    else:
                        print(f"Player 2, would you like to remove 1, 2, or 3 stones? ", end='')
                        stones_to_remove = get_valid_stone_count(1, 3, stones_remaining)

                stones_remaining -= stones_to_remove
                print()
                time.sleep(1)  # Pause for readability

                if stones_remaining > 0 and stones_remaining % 3 == 0:
                    print(f"Since {stones_remaining} is divisible by 3, Player {current_player} must go again.")
                else:
                    current_player = 2 if current_player == 1 else 1

            if winner_by_last_stone:
                winning_player = 2 if current_player == 1 else 1
            else:
                winning_player = current_player

            winning_player_name = "AI" if opponent_type == "AI" and winning_player == 2 else f"Player {winning_player}"
            scores[winning_player_name] += 1

            print(f"Round {round_number} result: {winning_player_name} wins!\n")
            time.sleep(1.5)

            # Ask if the user wants to continue after each round.
            continue_playing = input("Do you want to continue to the next round? (yes/no): ").strip().lower()
            if continue_playing not in ['yes', 'y']:
                break

        print("Final scores after all rounds:")
        for player, score in scores.items():
            print(f"{player}: {score}")

        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("Exiting the game of Nimm...")
            time.sleep(2)
            print("")
            print("Goodbye!")
            time.sleep(0.9)
            break

    time.sleep(1)

def choose_opponent():
    # Asks the user to choose between playing with a friend or the AI.
    while True:
        choice = input("Do you want to play with a friend (f) or the AI (ai)? ").strip().lower()
        if choice in ["f", "friend", "ai"]:
            return "friend" if choice in ["f", "friend"] else "AI"
        else:
            print("Invalid choice. Please enter 'f' for friend or 'ai' for AI.")

def get_valid_stone_count(min_value, max_value, stones_remaining):
    # Gets a valid number of stones to remove from user input.
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
    # Asks the user if the winner should be the player who takes the last stone.
    while True:
        choice = input("Should the winner be the player who takes the last stone (y/n)? ").strip().lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def select_total_stones():
    # Asks the user to select the total number of stones (between 20 and 100).
    while True:
        try:
            total_stones = int(input("Select the number of stones (between 20 and 100): ").strip())
            if 20 <= total_stones <= 100:
                return total_stones
            else:
                print("Please enter a number between 20 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def intelligent_ai_choice(stones_remaining):
    # Intelligently decides the number of stones the AI should remove.
    if stones_remaining > 3:
        return (stones_remaining - 1) % 4 or random.randint(1, 3)
    else:
        return stones_remaining

##########################################################################
"""The Number Guess Game"""

def guess_game_num():
    while True:
        # Generate a random secret number between 1 and 99.
        secret_number = random.randint(1, 99)
        print("I am thinking of a number between 1 and 99...")
        time.sleep(1)

        # Prompt the user for a guess and initialize the guess variable.
        guess = None
        while guess != secret_number:
            guess = input("Enter a guess: ")

            # Check if the input is an empty string.
            if guess == "":
                print("Input cannot be empty. Please enter a number.")
                time.sleep(1)
                continue

            # Convert the input to an integer.
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)
                continue

            # Check if the guess is too low or too high.
            if guess < secret_number:
                print("Your guess is too low!")
            elif guess > secret_number:
                print("Your guess is too high!")

        # The loop exits when the user guesses the correct number.
        print("")
        print(f"Congrats! The number was {secret_number}.\n")
        print(f"Thanks for playing!\n")
        time.sleep(1)

        # Ask user if they want to play again or return to the menu
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            continue  # Restart the game loop
        elif choice == 'no':
            print("Exiting Guess Game...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue

##########################################################################
"""The High-Low Game"""


NUM_ROUNDS = 5
def high_low_game():
    # Welcome message.
    print("Welcome to the High-Low Game!")
    time.sleep(1)
    print('--------------------------------')
    time.sleep(1)

    # Loop for the game sessions.
    while True:
        score = 0
        
        # Loop for the number of rounds.
        for round_num in range(1, NUM_ROUNDS + 1):
            score = play(round_num, score)
            print()
            time.sleep(1)

        # Print final message based on the score.
        print_final_message(score)
        time.sleep(1)

        # Ask user if they want to play again.
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            print("Loading...")
            print("")
            time.sleep(1)
            continue  # Restart the game loop
        elif choice == 'no':
            print("Exiting High-Low Game...")
            time.sleep(1)
            return
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    # Return to the main menu.
    return_to_menu()

def play(round_num, score):
    # Generate random numbers for the user and computer.
    num_user = random.randint(1, 100)
    num_computer = random.randint(1, 100)

    # Display round number and user's number.
    print(f"Round {round_num}")
    print(f"Your number is {num_user}")
    time.sleep(0.5)

    while True:
        # Get user's guess and validate input.
        user_answer = input("Do you think your number is higher or lower than the computer's?: ").lower()

        while user_answer not in ["higher", "lower"]:
            user_answer = input("Please enter either 'higher' or 'lower': ").lower()
            time.sleep(0.5)

        # Check if user's guess is correct and update score accordingly.
        if num_user < num_computer:
            correct_answer = "lower"
        elif num_user > num_computer:
            correct_answer = "higher"
        else:
            print(f"It's a tie! Let's try again for round {round_num}.")
            continue  # Restart the loop to ask the user again

        if user_answer == correct_answer:
            print(f"You were right! The computer's number was {num_computer}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {num_computer}")

        break  # Exit the loop if the user has given a valid answer

    # Print current score.
    print(f"Your score is now {score}")
    return score

def print_final_message(score):

    # Print final message based on the score.
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!\nThanks for Playing!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!\nThanks for Playing!")
    else:
        print("Better luck next time!\nThanks for Playing!")

##########################################################################
"""Planetary Weight Calculator"""


"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

"""
def planetary_weight_calculator():
    print("This program converts age in human years to equivalent cat years.")
    time.sleep(1)
    # Prompt user for Earth weight
    earth_weight_input_str = input("Enter a weight on Earth: ")
    # Convert Earth weight to a float
    earth_weight = float(earth_weight_input_str)
    time.sleep(0.8)
    # Prompt user for planet choice
    planet_choice_str = input("Enter a planet in our solar system: ").lower()  # Convert to lowercase
    
    time.sleep(0.8)

    # Initialize weight in case none of the if conditions below are true.
    weight = 0

    # Check the user's planet choice and calculate the equivalent weight
    if planet_choice_str == "mars":
        weight = earth_weight * MARS
    elif planet_choice_str == "mercury":
        weight = earth_weight * MERCURY
    elif planet_choice_str == "venus":
        weight = earth_weight * VENUS
    elif planet_choice_str == "jupiter":
        weight = earth_weight * JUPITER
    elif planet_choice_str == "saturn":
        weight = earth_weight * SATURN
    elif planet_choice_str == "uranus":
        weight = earth_weight * URANUS
    elif planet_choice_str == "neptune":
        weight = earth_weight * NEPTUNE
    elif planet_choice_str == "earth":
        weight = earth_weight * EARTH
    else:
        print("Invalid planet name")
        time.sleep(1)
        return

    # Round weight to 2 decimal places
    weight = round(weight, 2)
    # Print the equivalent weight on the chosen planet
    print(f"The equivalent weight on {planet_choice_str}: {str(weight)}")
    time.sleep(1)

    # Ask user if they want to convert another weight or quit
    while True:
        choice = input("Do you want to convert another weight? (yes/no): ").strip().lower()
        if choice == 'yes':
           planetary_weight_calculator() 
        elif choice == 'no':
            print("Exiting...")
            time.sleep(1)
            return
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            
    time.sleep(1)

##########################################################################
"""Cat Years"""

def cat_years():
    try:
        # Converts a user's age in human years to equivalent cat years.
        print("This program converts age in human years to equivalent cat years.")
        human_years_str = input("Enter your age in human years: ")
        human_years = float(human_years_str)
        time.sleep(0.5)
        cat_years = human_years * CAT_YRS_MULTIPLIER
        print(f"You are {cat_years:.1f} years old in cat years!")
    except ValueError:
        print("Invalid input. Please enter a number for your age.")
    time.sleep(1)

##########################################################################
"""Dog Years"""

def dog_years():
    #This program converts age in human years to age in dog years.
    try:
        print("This program converts age in human years to age in dog years.")
        time.sleep(1)
        human_years = input("Enter an age in calendar years: ")
        human_years = float(human_years)
        time.sleep(0.5)
        total = human_years * DOG_YRS_MULTIPLIER
        print("Loading...")
        time.sleep(1.2)
        print("That's " + str(total) + " in dog years!")
    except ValueError:
        print("Invalid input. Please enter a number for your age.")
    time.sleep(1)

    while True:
        choice = input("Do you want to run Dog Years again? (yes/no): ").strip().lower()
        if choice == 'yes':
            print("Loading...")
            time.sleep(1)
            print("")
            dog_years()
            break
        elif choice == 'no':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            time.sleep(1)

##########################################################################

# Return to menu or quit function.
def return_to_menu():
    while True:
        choice = input("Do you want to return to the main menu or quit OH-MEGA? (menu/quit): ").strip().lower()
        if choice == 'menu':
            return True
        elif choice == 'quit':
            print("Exiting program...")
            time.sleep(1)
            print("Thank you for using OH-MEGA!")
            print("Goodbye!")
            time.sleep(1)
            return False
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    # Display program options.
    while True:
        print("\nWhich program would you like to run?\n")
        time.sleep(0.4)
        print("1. Wholesome Machine")
        time.sleep(0.4)
        print("2. The QuizMaster")
        time.sleep(0.4)
        print("3. Atlas: The Capital Guessing Game")
        time.sleep(0.4)
        print("4. The Math Practice Program")
        time.sleep(0.4)
        print("5. The Game of Nimm")
        time.sleep(0.4)
        print("6. Number Guess Game")
        time.sleep(0.4)
        print("7. High-Low Game")
        time.sleep(0.4)
        print("8. Planetary Weight Calculator")
        time.sleep(0.4)
        print("9. Cat Years")
        time.sleep(0.4)
        print("10. Dog Years")
        time.sleep(0.4)
        print("0. Exit")

        # Get user choice.
        choice = input("Enter your choice (0-10): ")

        if choice == "0":
            # Exit the program.
            print("Thank you for using OH-MEGA!")
            print("Goodbye!")
            time.sleep(1)
            break  # Exit the while loop and end the program

        elif choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            # Dictionary mapping user input to corresponding function.
            program_funcs = {
                "1": wholesome_machine,
                "2": quizmaster,
                "3": atlas,
                "4": math_practice,
                "5": game_of_nimm,
                "6": guess_game_num,
                "7": high_low_game,
                "8": planetary_weight_calculator,
                "9": cat_years,
                "10": dog_years     
            }

            program_func = program_funcs.get(choice)
            if program_func:
                # Execute the selected program function.
                program_func()
                # Ask user if they want to return to the main menu or quit.
                if not return_to_menu():
                    break
        # Handle invalid user input.
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == '__main__':
    # Display welcome message only when the program starts.
    print("Welcome to OH-MEGA!")
    time.sleep(1.5)
    print("Created by Rishav Dey for Code in Place 2024's final project.")
    time.sleep(1.5)

    main_menu()
