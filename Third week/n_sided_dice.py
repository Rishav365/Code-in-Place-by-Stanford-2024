import random

def main():
    # This program takes as input the number of sides on a dice.  Then, simulate rolling a dice with that many sides.
    sides = input("How many sides does your dice have?")
    sides = int(sides)
    total = random.randint(1,sides)
    print("Your roll is " + str(total))

if __name__ == '__main__':
    main()