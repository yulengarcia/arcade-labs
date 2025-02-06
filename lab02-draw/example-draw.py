"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade
from pyglet.libs.win32.constants import lDefaultTab

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.ARSENIC)

# --- Draw the barn ---

# Draw the clouds
arcade.draw_circle_filled(600, 450, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(550, 475, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(600, 482, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(650, 475, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(700, 450, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(650, 425, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(600, 417, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(550, 425, 50, arcade.color.OLD_LACE)
arcade.draw_circle_filled(500, 450, 50, arcade.color.OLD_LACE)


# Barn cement base
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.GREEN)

# Bottom half
arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

# Left-bottom window
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

# Right-bottom window
arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)

# Barn door
arcade.draw_rectangle_filled(190, 230, 100, 100, arcade.color.BLACK_BEAN)

# Rail above the door
arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BONE)

# Draw second level of barn
arcade.draw_polygon_filled([[20, 350],
                            [100, 470],
                            [280, 470],
                            [360, 340]],
                            arcade.color.BROWN)

# Draw loft of barn
arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)

# Left-top window
arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)

# Right-top window
arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.BLACK)

# Draw 2nd level door
arcade.draw_rectangle_outline(190, 310, 30, 60, arcade.color.BONE, 5)

# --- Finish drawing --
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

