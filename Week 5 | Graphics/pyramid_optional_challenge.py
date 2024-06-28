"""

Brick Pyramid Drawing

Author: Rishav Dey
Date: 25th May 2024
Version: 1.0

Description:

A program that draws a pyramid consisting of bricks arranged in horizontal rows, so that the number of bricks in each row decreases by one as you move up the pyramid. 

"""

from graphics import Canvas

# Constants for the canvas size and brick dimensions.
CANVAS_WIDTH = 600  # Width of drawing canvas in pixels.
CANVAS_HEIGHT = 300  # Height of drawing canvas in pixels.
BRICK_WIDTH = 30  # The width of each brick in pixels.
BRICK_HEIGHT = 12  # The height of each brick in pixels.
BRICKS_IN_BASE = 14  # The number of bricks in the base.

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)  # Creates a canvas.
    draw_pyramid(canvas)  # Draw the pyramid on the canvas.

def draw_pyramid(canvas):
    # Calculates the starting x-coordinate for centering the pyramid.
    start_x = (CANVAS_WIDTH - BRICKS_IN_BASE * BRICK_WIDTH) // 2

    # Draw each row of bricks from bottom to top.
    for row in range(BRICKS_IN_BASE):
        # Calculates the y-coordinate for the current row.
        y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT
        # Draws the current row of bricks.
        draw_row(canvas, start_x, y, BRICKS_IN_BASE - row)

def draw_row(canvas, start_x, y, bricks):
    # Calculates the starting x-coordinate for centering the row.
    x = start_x + (BRICKS_IN_BASE - bricks) * BRICK_WIDTH // 2

    # Draws each brick in the row.
    for i in range(bricks):
        draw_brick(canvas, x, y, "yellow")  # Draws a brick with yellow color.
        x += BRICK_WIDTH  # Move to the position of the next brick.

def draw_brick(canvas, x, y, color):
    # Draws a single brick as a rectangle.
    canvas.create_rectangle(
        x, y,
        x + BRICK_WIDTH, y + BRICK_HEIGHT,
        color=color, outline="black"
    )

if __name__ == '__main__':
    main()
