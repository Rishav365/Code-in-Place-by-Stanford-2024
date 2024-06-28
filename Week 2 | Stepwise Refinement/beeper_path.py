"""

Karel was trying to get back home but got lost! 
Luckily, they set a path of beepers down as they were traveling earlier.

"""

from karel.stanfordkarel import *

# Helping Karel get back home:

def main():
    # Pre: Karel is at the beginning of a straight line of beepers and is facing east.
    # Post: Karel moves forward along the line of beepers until reaching the end or encountering a wall, at which point Karel stops.
    while beepers_present() and front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()