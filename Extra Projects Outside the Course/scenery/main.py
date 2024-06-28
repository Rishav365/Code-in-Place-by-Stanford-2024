"""
Scenic Drawing Program

Author: Rishav Dey
Date: 22nd May 2024 
Version: 1.0

Description:
This program creates a scenic drawing of a countryside using the graphics module. It includes elements such as 
sky, grass, sun, clouds, houses, and sheep. Each element is drawn on a canvas with specified dimensions and colors.

Libraries Used:
- graphics: A custom module for handling graphical operations.

Usage:
Ensure the graphics module is correctly imported and accessible. Adjust the CANVAS_WIDTH and CANVAS_HEIGHT constants
to modify the dimensions of the canvas. Run the script to display the scenic drawing with various elements placed 
randomly or at specific coordinates.

Notes:
- Click anywhere on the canvas to exit the program.
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SKY_COLOR = "lightblue"
GRASS_COLOR = "limegreen"
SUN_COLOR = "yellow"
CLOUD_COLOR = "white"

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw sky
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color=SKY_COLOR)
    
    # Draw grass
    canvas.create_rectangle(0, CANVAS_HEIGHT//2, CANVAS_WIDTH, CANVAS_HEIGHT, color=GRASS_COLOR)
    
    # Draw sun
    sun_radius = 50
    canvas.create_oval(50, 50, 50 + 2*sun_radius, 50 + 2*sun_radius, color=SUN_COLOR)
    
    # Draw clouds
    draw_cloud(canvas, 100, 100)
    draw_cloud(canvas, 300, 150)
    draw_cloud(canvas, 600, 120)
    
    # Draw houses
    draw_house(canvas, 100, CANVAS_HEIGHT//1.7 - 100, "red")  # Regular house
    draw_farm(canvas, 500, CANVAS_HEIGHT//1.7 - 120)  # Farm-style house
    
    # Draw sheep
    for _ in range(5):
        x = random.randint(200, CANVAS_WIDTH - 100)
        y = random.randint(CANVAS_HEIGHT//2 + 50, CANVAS_HEIGHT - 50)
        draw_sheep(canvas, x, y)
    
    canvas.wait_for_click()

def draw_cloud(canvas, x, y):
    cloud_width = 80
    cloud_height = 40
    canvas.create_oval(x, y, x + cloud_width, y + cloud_height, color=CLOUD_COLOR)
    canvas.create_oval(x + 40, y - 10, x + cloud_width + 40, y + cloud_height - 10, color=CLOUD_COLOR)

def draw_house(canvas, x, y, roof_color):
    # House body
    canvas.create_rectangle(x, y, x + 80, y + 60, color="tan")
    # Roof
    canvas.create_polygon(x - 10, y, x + 40, y - 30, x + 90, y, color=roof_color)
    # Door
    canvas.create_rectangle(x + 30, y + 30, x + 50, y + 60, color="brown")
    # Window
    canvas.create_rectangle(x + 10, y + 10, x + 25, y + 25, color="tan")

def draw_farm(canvas, x, y):
    # Barn body
    canvas.create_rectangle(x, y, x + 120, y + 80, color="red")
    # Roof
    canvas.create_polygon(x - 10, y, x + 60, y - 40, x + 130, y, color="darkred")
    # Door
    canvas.create_rectangle(x + 45, y + 40, x + 75, y + 80, color="brown")
    # Windows
    canvas.create_rectangle(x + 20, y + 20, x + 40, y + 40, color="yellow")
    canvas.create_rectangle(x + 80, y + 20, x + 100, y + 40, color="yellow")
    # Silo
    canvas.create_rectangle(x + 130, y + 20, x + 150, y + 80, color="gray")
    canvas.create_polygon(x + 125, y + 20, x + 140, y, x + 155, y + 20, color="silver")

def draw_sheep(canvas, x, y):
    # Body
    canvas.create_oval(x, y, x + 40, y + 30, color="white")
    # Head
    canvas.create_oval(x + 30, y - 10, x + 50, y + 10, color="white")
    # Legs
    for i in range(4):
        leg_x = x + 5 + i * 10
        canvas.create_line(leg_x, y + 25, leg_x, y + 35, color="black")

if __name__ == "__main__":
    main()