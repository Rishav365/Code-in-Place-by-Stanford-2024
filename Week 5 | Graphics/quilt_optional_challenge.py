"""

Patch Grid Drawing

Author: Rishav Dey
Date: 24th May 2024
Version: 1.0

Description:

A quilt, as you may know, is a blanket often composed of repeating "patches".
This Python script utilizes the 'graphics' module to draw a 2x4 grid of patches on a canvas. Each patch consists of either a circle or a square with specific colors and configurations:
- Circle patches are colored in salmon.
- Square patches have a purple frame with a smaller inset white square inside.

"""


from graphics import Canvas

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
   canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

   # draw the first row of patches
   draw_square_patch(canvas, 0, 0)
   draw_circle_patch(canvas, PATCH_SIZE, 0)
   draw_square_patch(canvas, PATCH_SIZE * 2, 0)
   draw_circle_patch(canvas, PATCH_SIZE * 3, 0)

   # Second row
   draw_circle_patch(canvas, 0, PATCH_SIZE)
   draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
   draw_circle_patch(canvas, PATCH_SIZE * 2, PATCH_SIZE)
   draw_square_patch(canvas, PATCH_SIZE * 3, PATCH_SIZE)

def draw_circle_patch(canvas, start_x, start_y):
   # Draw a circle
   center_x = start_x + PATCH_SIZE // 2
   center_y = start_y + PATCH_SIZE // 2
   radius = PATCH_SIZE // 2
   canvas.create_oval(start_x, start_y, start_x + PATCH_SIZE, start_y + PATCH_SIZE, color='salmon', outline='')

def draw_square_patch(canvas, start_x, start_y):
   # draws a purple frame at (start_x, start_y)
   end_x = start_x + PATCH_SIZE
   end_y = start_y + PATCH_SIZE
   inset = 20
   # first draw a purple square over the entire patch
   canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
   # then draw a smaller white square on top
   canvas.create_rectangle(start_x + inset, start_y + inset, end_x - inset, end_y - inset, 'white')

if __name__ == '__main__':
   main()