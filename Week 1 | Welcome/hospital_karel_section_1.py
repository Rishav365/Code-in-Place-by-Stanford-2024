from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():

#   Karel builds hospitals at specified locations.
#   Pre: Karel starts at (1, 1) facing east with an infinite number of beepers in its beeper bag.
#   Post: Karel finishes building hospitals and stops when a wall is in front.

    move_until_wall_or_beeper()
    detect_and_build_hospitals()
    move_until_wall_or_beeper()
    detect_and_build_hospitals()
    move_until_wall_or_beeper()
    detect_and_build_hospitals()

 
def move_until_wall_or_beeper():
    # Moves Karel forward until it hits a wall or detects a beeper.
    # Pre: Karel is facing east with no wall in front.
    # Post: Karel stops when it encounters a wall or a beeper
    while no_beepers_present() and front_is_clear():
        move()

#   Detects beepers and builds hospitals at the detected locations.
#   Pre: Karel is facing east with no wall in front.
#   Post: Karel stops when it encounters a wall or a no beeper is present.
def detect_and_build_hospitals():
    while beepers_present() and front_is_clear():
        build_hospital()


def build_hospital():
    # Builds a hospital at the current location.
    # Pre: Karel is facing east with beepers present.
    # Post: Karel finishes building the hospital and moves to the next location if front is clear.
    pick_beeper()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    fence_post_fix()


#   Eliminates the fence post problem.
def fence_post_fix():
    while front_is_clear() and beepers_present():
        move()      
    

#   Makes Karel turn left thrice! To make her turn right(oh, the struggle Karel has to go through...)
def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()