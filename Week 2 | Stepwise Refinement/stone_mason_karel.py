from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    # Karel builds the missing columns in the Temple of Artemis.
    # Pre: Karel starts at the bottom left corner, facing right(east).
    # Post: Karel finishes building the columns and stops facing east.

    # Karel builds each column one by one.
    for i in range(4):
        build_column()
    

def build_column():
    #Karel builds a single column in the Temple of Artemis.
    #Pre: Karel is at the bottom of a column, facing east.
    #Post: Karel finishes building the column and moves to the next position to the right.
    put_beeper()
    turn_left()
    repeat_stone()
    turn_180()
    return_to_base()
    # If there is a clear path in front of Karel, she moves to the next column, else she stops.
    if front_is_clear():
        for i in range(4):
            move()

def repeat_stone():
    #  Karel repeats placing a stone(beeper)until reaching the top of the column.
    #  Pre: Karel is at the base of a column, facing north.
    #  Post: Karel finishes building the column, facing north.
    while front_is_clear():
        move()
        put_beeper()

def return_to_base():
    # Karel returns to the base of the column.
    # Pre: Karel is at the top of a column, facing south.
    # Post: Karel returns to the base of the column, facing east.
    while front_is_clear():
        move()
    turn_left()
        
def turn_180():
    # Karel turns around 180 degrees.
    # Pre: Karel is at the top of a column, facing north.
    # Post: Karel is at the top of the column, facing south.
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()