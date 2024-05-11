"""
Uses constants to tell a mad libs story.
"""

# Fun fact: 6174 is known as Kaprekar's constant,
# and it's a pretty mysterious number :)

# Constants
WIZARD = 'Karel'  # The name of the wizard in the story
NUMBER_OF_FRUIT = 6174  # The number of fruit the wizard has
FRUIT = 'mangoes'  # The type of fruit the wizard loves to eat

def main():
    # Prints the story using the constants
    print("There once was a wizard by the name of " + WIZARD + " who loved to eat " + FRUIT + ".")
    print(WIZARD + " always kept a stash of " + str(NUMBER_OF_FRUIT) + " " + FRUIT + " in their house...")

if __name__ == '__main__':
    main()