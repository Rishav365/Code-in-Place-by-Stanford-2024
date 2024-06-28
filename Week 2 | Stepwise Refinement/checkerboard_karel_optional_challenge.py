from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    # Karel fills the world with beepers in a checkerboard pattern.
    # Pre: Karel starts at the bottom-left corner of the world, facing east.
    # Post: Karel fills the world with beepers in a checkerboard pattern and ends where she started from.
    if left_is_blocked():
        put_beeper()
    else:
        if front_is_blocked():
            turn_left()
            fill_row()
        else:
            while left_is_clear():
                fill_row()
                turn_left()
                do_next_row()
            fence_post_fix()

    if facing_east():
        turn_180()
    else:
        turn_180()
        move()
        move()
        turn_right()

    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()


def fill_row():
    # Karel fills a row with beepers in a checkerboard pattern.
    # Pre: Karel is at the leftmost part of a row, facing east.
    # Post: Karel finishes placing beepers in the row and moves to the rightmost part, facing east.
    while front_is_clear():
        put_beeper()
        for i in range(2):
            if front_is_clear():
                move()
    one_step_back()
    if no_beepers_present():
        one_step_back()
        put_beeper()
    else:
        one_step_back()


def step_up():
    # Karel moves up to the next row and starts placing beepers.
    # Pre: Karel is at the bottom of a row, facing north.
    # Post: Karel moves to the next row and starts placing beepers, facing west.
    if no_beepers_present():
        move()
        put_beeper()
        turn_left()
    else:
        move()
        turn_left()


def relocate():
    # Karel repositions itself for placing the next row of beepers.
    # Pre: Karel is at the end of a row, facing west.
    # Post: Karel moves to the appropriate position to start the next row, facing west.
    if no_beepers_present():
        move()
    else:
        move()
        if front_is_clear():
            move()


def do_next_row():
    # Karel moves up to the next row and starts placing beepers.
    # Pre: Karel is at the bottom of a row, facing north.
    # Post: Karel moves to the next row and starts placing beepers, facing west.
    if front_is_clear():
        step_up()
        relocate()
        fill_row()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_right()

def turn_180():
    # Karel turns around 180 degrees.
    # Pre: Karel is at the top of a column, facing north.
    # Post: Karel is at the top of the column, facing south.
    for i in range(2):
        turn_left()

def turn_right():
    # Makes Karel turn left thrice! To make her turn right...
    for i in range(3):
        turn_left()

def one_step_back():
    # Karel moves backwards.
    # Pre: Karel can be in any can be positioned anywhere and is either in facing east or west direction.
    # Post: Karel moves one step backward from its current position and is facing in the opposite direction.
    turn_180()
    move()

def fence_post_fix():
    # Karel checks the last row for fence-post error and places a beeper if necessary.
    # Pre: Karel has finished placing beepers in all rows and is facing east.
    # Post: Karel places a beeper if there is a missing one at the end of the last row.
    move()
    if no_beepers_present():
        one_step_back()
        turn_180()
        fill_row()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()