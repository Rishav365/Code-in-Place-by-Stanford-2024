from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 24 beepers, and end facing East to 
the right of the 24 beepers.
"""
#Karel's way of welcoming you to Code in Place 2024!

def main():
    # Pre: Karel starts at (1, 1) facing East with an infinite number of beepers in its beeper bag.
    # Post: Karel places 20 beepers, then 24 beepers, and ends facing East to the right of the 24 beepers.
    for i in range(20):
        put_beeper()
    move()
    for i in range(24):
        put_beeper()
    move()
    
if __name__ == '__main__':
    main()