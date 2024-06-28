"""
Random Circles

Description:

This Python script generates a random number of circles on a graphical canvas 
using the graphics library. Each circle is positioned randomly within the canvas 
boundaries and is filled with a random color chosen from a predefined set. The size 
of each circle is also randomly determined. This project demonstrates basic graphical 
manipulation and randomness in Python programming, offering a simple yet illustrative 
example of generating visual elements dynamically.
"""
from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = random.randint(1, 50)
N_CIRCLES = random.randint(1, 20)



def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)

def draw_random_circle(canvas):
    x = random.randint(0, CANVAS_WIDTH-CIRCLE_SIZE)
    y = random.randint(0, CANVAS_HEIGHT-CIRCLE_SIZE)
    color = random_color()
    canvas.create_oval(x, y, x+CIRCLE_SIZE, y+ CIRCLE_SIZE, color)
    
def random_color():
    """
    This is a function to use to get a random color for each circle.
    This code was pre-defined. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()