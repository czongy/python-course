# import colorgram
#
# colors = colorgram.extract('spot_painting.jpg', 30)
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

import turtle as turtle_mod
from random import choice

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64),
              (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
              (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216),
              (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179), (122, 169, 190), (29, 85, 93),
              (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]
turtle_mod.colormode(255)
tim = turtle_mod.Turtle()
tim.penup()
tim.ht()
tim.speed("fastest")

for i in range(-250, 250, 50):
    tim.setpos(-250, i)
    for n in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)

screen = turtle_mod.Screen()
screen.exitonclick()