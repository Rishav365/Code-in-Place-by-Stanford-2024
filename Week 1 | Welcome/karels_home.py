from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    # Pre: Karel is about to go pick the beeper.
    # Post: Karel is now back home after picking up the beeper.
    move_2()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_left()
    turn_left()
    move_3()
    turn_right()
    move()
    turn_right()
     
def move_2():
    # Makes Karel move 2 steps at once!
    move()
    move()

def move_3():
    # Makes Karel move 3 steps at once!
    for i in range(3):
        move()

def turn_right():
    # Makes Karel left thrice! To make her turn right...
    for i in range(3):
        turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()