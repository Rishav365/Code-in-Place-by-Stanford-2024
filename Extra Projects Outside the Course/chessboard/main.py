"""
Chessboard Drawing Program

Author: Rishav Dey
Date: 25th May 2024
Version: 1.0

Description:
This program generates a chessboard pattern using the graphics module. It creates a canvas of specified dimensions,
divides it into rows and columns, and alternates the color of squares to resemble a chessboard pattern.

Libraries Used:
- graphics: A custom module for graphical operations.

Usage:
Ensure the graphics module is correctly imported and accessible. Adjust the CANVAS_WIDTH, CANVAS_HEIGHT, N_ROWS, and N_COLS
constants to modify the dimensions and size of the chessboard. Run the script to display the chessboard pattern on the canvas.
"""

from graphics import Canvas

# Define the canvas size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = CANVAS_WIDTH

# Define the number of rows and columns
N_ROWS = 8
N_COLS = N_ROWS
# Define the square size
SIZE = CANVAS_WIDTH / N_ROWS

def main():
    # Create the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw the chessboard
    draw_chessboard(canvas)

def draw_chessboard(canvas):
    # Iterate over the rows and columns
    for row in range(N_ROWS):
        for col in range(N_COLS):
            # Calculate the square coordinates
            x1 = col * SIZE
            y1 = row * SIZE
            x2 = x1 + SIZE
            y2 = y1 + SIZE

            # Determine the square color based on the row and column
            if (row + col) % 2 == 1:
                color = 'white'
            else:
                color = 'black'

            # Draw the square
            canvas.create_rectangle(x1, y1, x2, y2, color, 'black')

if __name__ == "__main__":
    main()