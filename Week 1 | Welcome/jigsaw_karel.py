from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""
#Karel's solution to Jigsaw:

def main():
    # Pre: Karel has a puzzle to complete! Karel's has to pick up the last puzzle piece from (row 1, column 3) and put the puzzle piece in place (row 3, column 4). 
    # Post: Karel has finally returned to her initial position after completing the puzzle.
    puzzle_finisher()
    completed_puzzle_admirer()
    

def puzzle_finisher():
    # Karel picks up the last puzzle piece and puts it where it should go.
    move()
    move()
    pick_beeper()
    # Karel has picked up the puzzle piece and will now proceed to the place where the puzzle should be put.
    move()
    turn_left()
    for i in range(2):
        move()
    # Karel has reached the location where the last puzzle piece should be and puts it there.
    put_beeper()

    
def completed_puzzle_admirer():
    # Karel has now completed the puzzle but wants to return to her intial postion so that she can admire her completed puzzle.
    # Pre: Karel is facing north in the last puzzle piece's location.
    # Post: Karel is back to her initial position. She admires her completed puzzle.
    for i in range(2):
        turn_left()
    move()
    move()
    turn_right()
    for i in range(3):
        move()
    turn_left()
    turn_left()


def turn_right():
    # Makes Karel turn left thrice! To make her turn right...
  for i in range(3):
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()