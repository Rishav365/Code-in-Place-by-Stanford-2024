"""
Georgian Flag Drawing Program

Author: Rishav Dey
Date: 26th May 2024
Version: 1.0

Description:
This program draws the flag of Georgia using the graphics module. It creates a canvas with specified dimensions,
draws a large red cross in the center, and smaller red crosses in each quadrant of the canvas.

Libraries Used:
- graphics: A custom module for handling graphical operations.

Usage:
Ensure the graphics module is correctly imported and accessible. Adjust the CANVAS_WIDTH and CANVAS_HEIGHT constants
to modify the dimensions of the flag as desired. Run the script to display the Georgian flag on the canvas.
"""

from graphics import Canvas

CANVAS_WIDTH = 400  # Increase the canvas width to accommodate the new flag design
CANVAS_HEIGHT = 300  # Adjust the canvas height as desired

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_georgian_flag(canvas)
    canvas.wait_for_click()

def draw_georgian_flag(canvas):
    # Draw the background
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'white')

    # Draw the red cross
    draw_red_cross(canvas, CANVAS_WIDTH/2, CANVAS_HEIGHT/2, CANVAS_WIDTH/2, CANVAS_HEIGHT/2)

    # Draw the smaller crosses
    draw_small_red_crosses(canvas, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, CANVAS_WIDTH / 16, CANVAS_HEIGHT / 15)

def draw_red_cross(canvas, center_x, center_y, width, height):
    """Draw a red cross on the canvas."""
    left_x = center_x - width / 0.8
    right_x = center_x + width / 0.8
    top_y = center_y - height / 0.8
    bottom_y = center_y + height / 0.8

    canvas.create_rectangle(left_x, center_y - height / 10, right_x, center_y + height / 10, 'red')
    canvas.create_rectangle(center_x - width / 10, top_y, center_x + width / 10, bottom_y, 'red')

def draw_small_red_crosses(canvas, center_x, center_y, width, height):
    """Draw four smaller red crosses on the canvas."""
    offset_x = CANVAS_WIDTH / 3.7
    offset_y = CANVAS_HEIGHT / 4

    draw_red_cross(canvas, center_x - offset_x, center_y - offset_y, width, height)
    draw_red_cross(canvas, center_x + offset_x, center_y - offset_y, width, height)
    draw_red_cross(canvas, center_x - offset_x, center_y + offset_y, width, height)
    draw_red_cross(canvas, center_x + offset_x, center_y + offset_y, width, height)

if __name__ == '__main__':
    main()