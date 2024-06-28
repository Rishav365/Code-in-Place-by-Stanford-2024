"""
Canvas Box Drawing

Description:

This Python script utilizes the `graphics` module to draw a row of white rectangles 
on a canvas. Each rectangle represents a box with dimensions determined by the canvas 
width divided by the number of boxes (`N_BOXES`). The rectangles are drawn from left to 
right along the bottom edge of the canvas, with each rectangle having a black border.

"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH // N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw the boxes
    for i in range(N_BOXES):
        left_x = i * BOX_SIZE
        top_y = CANVAS_HEIGHT - BOX_SIZE
        right_x = left_x + BOX_SIZE
        bottom_y = CANVAS_HEIGHT
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "white", "black")

if __name__ == '__main__':
    main()