from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    # Pre: Karel is facing east with beepers to collect ahead.
    # Post: Karel has picked up all the beepers but has stopped as there's a wall in front.
    move()
    check_beepers()
        
    while front_is_clear():
        check_beepers()
        move()
   
def check_beepers():
    # Puts beepers at targeted locations.
    if beepers_present():
        for i in range(10):
            pick_beeper()
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()