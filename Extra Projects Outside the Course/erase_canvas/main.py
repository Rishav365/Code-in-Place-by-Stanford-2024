"""
Canvas Eraser Program

Author: Rishav Dey
Date: 29th May 2024
Version: 1.0

Description:
This program implements an 'eraser' on a canvas. The canvas consists of a grid of blue 'cells' represented as 
rectangles. The eraser, when dragged around the canvas, sets all rectangles it touches to white, effectively 
'erasing' parts of the canvas.

Libraries Used:
- graphics: A custom module for handling graphical operations.

Usage:
Ensure the graphics module is correctly imported and accessible. Adjust the CANVAS_WIDTH, CANVAS_HEIGHT, CELL_SIZE,
and ERASER_SIZE constants to modify the canvas and eraser dimensions as needed. Run the script to interactively
erase parts of the canvas by dragging the eraser rectangle.

Notes:
- Click on the canvas to place the eraser.
- Move the mouse to drag the eraser and erase parts of the canvas.
"""

from graphics import Canvas
import time
    
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_SIZE = 20
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y

    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

# There is no need to edit code beyond this point

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Figure out how many columns of cells we need
    
    # Make a grid of squares based on the number of rows and columns.
    # The rows and columns along with our cell size help determine where
    # each individual cell belongs in our grid!
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            
            # Create a single cell in the grid
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
            canvas.set_outline_color(cell, 'black')
            
    canvas.wait_for_click()  # Wait for the user to click before creating the eraser
    
    last_click_x, last_click_y = canvas.get_last_click()  # Get the starting location for the eraser
    
    # Create our eraser
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    while True:
        # Move the eraser, and erase what it's touching
        
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        erase_objects(canvas, eraser)  # We need to implement this!
        
        time.sleep(0.05)


if __name__ == '__main__':
    main()