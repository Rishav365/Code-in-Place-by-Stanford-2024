from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    # Karel spreads out a row of beepers and finds the midpoint.
    # Pre: Karel is at row 1, column 1, facing east, with the goal of finding the midpoint and placing a beeper there.
    # Post: Karel has finally found the midpoint and has successfully placed a beeper.
    place_beepers() # Karel places beepers.
             
    remove_ends() # Karel removes the beepers from both ends of the row.
                 
    finish()  # Karel is at the midpoint of the row facing east, with a beeper placed.
              
    if front_is_clear():
        move()
        if beepers_present():
            turn_180()
            move()
            pick_beeper()
            turn_180()
            move()
        else:
            turn_180()
            move()
            pick_beeper()
            move()
            turn_180()

    two_by_two() # This is to solve the midpoint puzzle in a 2x2 world.


def two_by_two():
    # If Karel encounters a 2x2 world, it picks up the beeper from the end and places it in the left most corner of the row.
    if front_is_blocked():
                           
        pick_beeper()
        turn_180()
        move()
        put_beeper()
        turn_180()

def place_beepers():
    # Karel places beepers.
    # Pre: Karel is at the beginning of a row facing east.
    # Post: Karel has placed a beeper and moved one step forward.
    put_beeper()
                   
    while front_is_clear(): 
                             
        move()
        put_beeper()

    turn_180()

def remove_ends():
    # Karel removes the beepers from both ends of the row.
    pick_beeper()
                   
    while front_is_clear():  
                             
        move()

    remove_end_beeper()  
                         
    trail_beeper_picker()


def remove_end_beeper():
    # Karel removes beepers present at both ends of a row.
    if beepers_present():
                            
        pick_beeper()

    if front_is_clear(): 
                          
        move()

    if no_beepers_present(): 
                               
        turn_180()

    if front_is_clear(): 
                          
        move()


def goToEnd():
    # Karel moves until she finds a beeper. If she encounters a beeper, she turns around.  
    while beepers_present():
        move()

    turn_180()
    move()
    

def finish():
    # Karel finishes by placing a beeper at the midpoint.
    # Pre: Karel is at the midpoint of the row facing east.
    # Post: Karel has placed the final beeper at the midpoint of the row facing east and has turned left.
    put_beeper()  
    while not_facing_east():
        turn_left() 
                               

def trail_beeper_picker():
    # Karel removes beepers along the row until it reaches the midpoint.
    while beepers_present():
        goToEnd()
        remove_end_beeper()


def turn_180():
    # Karel turns around 180 degrees.
    for i in range(2): 
        turn_left()

if __name__ == '__main__':
    main()