from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    # Draws the Indonesian flag
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw the red stripe (top half of the flag)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT / 2, "red")

if __name__ == '__main__':
    main()