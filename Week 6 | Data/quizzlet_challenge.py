"""
# Quizzlet - Spanish to English Translation Quiz

Author: Rishav Dey
Date: 27th May 2024
Version: 1.0

Description:

This Python script quizzes users on Spanish to English translations. It presents a series of English words and prompts 
the user to enter their Spanish translations. Feedback is provided for each answer, and at the end of the quiz, the total 
score is displayed along with an encouragement message.

"""

def main():
    # Dictionary containing English words and their Spanish translations
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0  # Initialise counter for correct answers
    total_count = len(translations)  # Total number of words to quiz
    
    # Loop through each English word and its Spanish translation
    for english_word, spanish_translation in translations.items():
        print(f"What is the Spanish translation for {english_word}?", end=" ")
        user_answer = input().strip().lower()
        
        # Check if the user's answer is correct
        if user_answer == spanish_translation:
            print("That is correct!\n")  # Correct answer feedback
            correct_count += 1  # Increment correct answer counter
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}.\n")
    
    # Print the final score and encouragement message.
    print(f"You got {correct_count}/{total_count} words correct, come study again soon!")

def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers

if __name__ == '__main__':
    main()
