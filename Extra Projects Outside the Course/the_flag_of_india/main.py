"""
Indian Flag Drawing Program

Author: Rishav Dey
Date: 25th May 2024
Version: 1.0

Description:
This program draws the flag of India using the graphics module. It consists of three horizontal stripes: 
saffron (orange), white, and green. Additionally, it includes the Ashoka Chakra, a wheel with 24 spokes, 
centered in the white stripe.

Libraries Used:
- graphics: A custom module for handling graphical operations.

Usage:
Ensure the graphics module is correctly imported and accessible. Adjust the CANVAS_WIDTH and CANVAS_HEIGHT 
constants to modify the dimensions of the canvas. Run the script to display the flag of India with its 
distinctive colors and Ashoka Chakra.

Notes:
- Click anywhere on the canvas to exit the program.
"""

from graphics import Canvas

CANVAS_WIDTH = 400  # Adjust the canvas width as desired
CANVAS_HEIGHT = 300  # Adjust the canvas height as desired

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_indian_flag(canvas)
    canvas.wait_for_click()

def draw_indian_flag(canvas):
    # Draws the orange stripe
    saffron_stripe_height = CANVAS_HEIGHT // 3
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, saffron_stripe_height, 'orange')

    # Draws the white stripe
    white_stripe_height = CANVAS_HEIGHT // 3
    canvas.create_rectangle(0, saffron_stripe_height, CANVAS_WIDTH, saffron_stripe_height + white_stripe_height, 'white')

    # Draws the green stripe
    green_stripe_height = CANVAS_HEIGHT // 3
    canvas.create_rectangle(0, saffron_stripe_height + white_stripe_height, CANVAS_WIDTH, CANVAS_HEIGHT, 'green')

    # Draws the Ashoka Chakra
    chakra_radius = white_stripe_height // 2
    chakra_center_x = CANVAS_WIDTH // 2.08
    chakra_center_y = saffron_stripe_height + white_stripe_height // 2
    draw_ashoka_chakra(canvas, chakra_center_x, chakra_center_y, chakra_radius)

def draw_ashoka_chakra(canvas, center_x, center_y, radius):
    """Draw the Ashoka Chakra on the canvas."""
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 'navy')

    # Draws the 24 spokes
    import math
    for i in range(24):
        angle = i * (360 / 24) 
        spoke_length = radius * 0.6
        spoke_x1 = center_x + radius * 0.2 * math.cos(math.radians(angle))
        spoke_y1 = center_y + radius * 0.2 * math.sin(math.radians(angle))
        spoke_x2 = center_x + radius * math.cos(math.radians(angle))
        spoke_y2 = center_y + radius * math.sin(math.radians(angle))
        canvas.create_line(spoke_x1, spoke_y1, spoke_x2, spoke_y2, 'white')

if __name__ == '__main__':
    main()