from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread_beeper them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""

def main():
    #Karel spreads the beepers along the row.
    #Pre: Karel starts at the beginning of the row, facing east, with a stack of beepers in front of her.
    #Post: Karel has spread_beeper out all the beepers along the row and stands at the end, facing east.
    move()
    spread_beeper()
    return_back()
    
def spread_beeper():
    # Karel picks up each beeper from the stack, moves to the end of the row, and places it down. 
    # This process continues until there are no more beepers in the stack.
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_end()
            put_beeper()
            reset_karel()
    put_beeper()
      
def move_to_wall():
    # Karel moves to the wall.
    while front_is_clear():
        move()

def move_to_end():
    # Karel moves to the end of the row while carrying a beeper.
    while beepers_present():
        move()

def reset_karel():
    # Karel resets its position after spreading a beeper.
    turn_around()
    move_to_wall()
    turn_around()
    move()

def turn_around():
    #Karel turns around 180 degrees.
    #Pre: Karel can be positioned anywhere and is either facing east or west.
    #Post: Karel is facing in the opposite direction from where she started.
    turn_left()
    turn_left()
    
def return_back():
    # Karel steps back to the starting position.
    turn_around()
    move()
    turn_around()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()