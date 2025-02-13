
import arcade

def sky():
# Tones of the sky
    arcade.draw_rectangle_filled(0,650,2000,300, arcade.color.AIR_FORCE_BLUE)
    arcade.draw_rectangle_filled(0,800,2000,300, arcade.color.BLUE_YONDER)


def sun():
    # Draw the sun
    arcade.draw_circle_filled(410, 250, 185, arcade.color.BURNT_ORANGE)
    arcade.draw_circle_filled(410, 250, 150, arcade.color.SAE)
    arcade.draw_circle_filled(410, 250, 115, arcade.color.AMBER)
    arcade.draw_circle_filled(410, 250, 80, arcade.color.CANARY_YELLOW)


def mountains():
    # Draw the mountains
    arcade.draw_triangle_filled(-75,300,50,550,175,300, arcade.color.BISTRE)
    arcade.draw_triangle_filled(12,475,50,550,88,475, arcade.color.AZURE_MIST)

    arcade.draw_triangle_filled(50,300,150,500,250,300, arcade.color.BROWN_NOSE)
    arcade.draw_triangle_filled(116,433,150,500,184,433, arcade.color.AZURE_MIST)


def grass():
    # Draw the grass
    arcade.draw_circle_filled(150, -50, 400, arcade.color.AO)
    arcade.draw_circle_outline(150, -50, 400, arcade.color.ARMY_GREEN)
    arcade.draw_circle_filled(800, -50, 500, arcade.color.AVOCADO)
    arcade.draw_circle_outline(800, -50, 500, arcade.color.ARMY_GREEN)


def clouds(x,y):
    # Big Cloud
    arcade.draw_circle_filled(300, 650, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(250, 675, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(300, 682, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(350, 675, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(400, 650, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(350, 625, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(300, 617, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(250, 625, 50, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(200, 650, 50, arcade.color.OLD_LACE)

    # Small Cloud
    arcade.draw_circle_filled(x, y, 20, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x+20, y+10, 20, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x+40, y+20, 20, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x+60, y+10, 20, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x+80, y, 20, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x+60, y-10, 20, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x+40, y-20, 20, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x+20, y-10, 20, arcade.color.OLD_LACE)


def birds():
    # Left Bird
    arcade.draw_line(255,632,260,640, arcade.color.BLACK)
    arcade.draw_line(260,640,290,620, arcade.color.BLACK)
    arcade.draw_line(290,620,320,640, arcade.color.BLACK)
    arcade.draw_line(320,640,325,632, arcade.color.BLACK)
    arcade.draw_circle_filled(290,620,4.5,arcade.color.BLACK)

    # Right Bird
    arcade.draw_line(307,654,310,660, arcade.color.BLACK)
    arcade.draw_line(310,660,330,650, arcade.color.BLACK)
    arcade.draw_line(330,650,350,660, arcade.color.BLACK)
    arcade.draw_line(350,660,353,654, arcade.color.BLACK)
    arcade.draw_circle_filled(330,650,4,arcade.color.BLACK)


def pine():
    # Draw the pine
    arcade.draw_rectangle_filled(850, 350,25,  80, arcade.color.BROWN_NOSE)
    arcade.draw_rectangle_filled(875, 350,25,  80, arcade.color.BISTRE)
    arcade.draw_triangle_filled(787,350,862,700,937,350,arcade.color.BRITISH_RACING_GREEN)

    arcade.draw_rectangle_filled(710, 275,15,  80, arcade.color.BROWN_NOSE)
    arcade.draw_rectangle_filled(725, 275,15,  80, arcade.color.BISTRE)
    arcade.draw_triangle_filled(660,275,720,600,780,275,arcade.color.BRUNSWICK_GREEN)

def on_draw(delta_time):
    arcade.start_render()

    sky()
    sun()
    mountains()
    grass()
    clouds(on_draw.mov_x, 625)
    birds()
    pine()

    on_draw.mov_x += 1

on_draw.mov_x = 550


def main():
    arcade.open_window(1000, 800, "Drawing Example")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()

