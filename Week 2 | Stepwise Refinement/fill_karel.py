from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    # Karel's main task: to fill the entire world with beepers.
    # Pre: Karel starts at the bottom-left corner, facing right (east).
    # Post: Karel finishes filling the world with beepers, ending at the top-right corner, facing right (east).
    fill_row()
    back_to_start()
    
def fill_row():
    # Karel moves along the current row, placing a beeper.
    # Pre: Karel is at the beginning of a row, facing east with a row to fill.
    # Post: Karel has filled the row with beepers and is at the end of the row, facing east.
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
        
def back_to_start():
    # Karel returns to the starting position(the left most corner of a row).
    # Pre: Karel is at the end of the row(right most corner of a row), facing east.
    # Post: Karel is at the starting of the row(the left most corner of a row).
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    turn_right()
    # Moves Karel up a row if top is clear.
    step_up()
    
def step_up():
    # Karel moves up to the next row and fills it with beepers.
    # Pre: Karel is at the leftmost corner of a row, facing north.
    # Post: If there is a row above and a path for Karel, Karel moves to that row and starts filling it with beepers. Otherwise, Karel ends at the rightmost corner, facing east.
    if front_is_clear():
        move()
        turn_right()
        fill_row()
        back_to_start()
    else:
        turn_right()
        while front_is_clear():
            move()

def turn_right():
    # Makes Karel turn left thrice! To make her turn right...
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()