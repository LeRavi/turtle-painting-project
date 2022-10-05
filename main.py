import turtle
import random
import colorgram
from turtle import Turtle
turtle.colormode(255)

# colors = colorgram.extract('image1.jpg', 100)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

number_of_dots = 100


def panting_line(dots):
    for dot_count in range(1, dots + 1):
        panting.dot(20, random.choice(color_list))
        panting.forward(50)

        if dot_count % 10 == 0:
            panting.setheading(90)
            panting.forward(50)
            panting.setheading(180)
            panting.forward(500)
            panting.setheading(0)


panting = Turtle()
panting.speed("fastest")
panting.penup()
panting.hideturtle()
color_list = [(244, 237, 229), (219, 148, 86), (245, 231, 236), (51, 106, 137), (153, 84, 54), (233, 243, 238), (219, 231, 238), (121, 162, 188), (144, 66, 93), (219, 86, 59), (204, 128, 154), (166, 152, 44), (51, 123, 85), (199, 85, 117), (26, 51, 77), (73, 160, 122), (116, 181, 152), (230, 201, 113), (40, 56, 108), (52, 42, 30), (55, 36, 51), (121, 34, 56), (241, 159, 183), (102, 120, 169), (47, 159, 179), (247, 167, 154), (26, 54, 41), (8, 102, 76), (112, 43, 34), (154, 212, 188), (144, 213, 224), (181, 183, 215), (12, 93, 106), (75, 74, 36), (238, 196, 11)]
direction = [0, 90, 180, 270]

panting.setheading(225)
panting.forward(400)
panting.setheading(0)
panting_line(100)


turtle.Screen()
turtle.exitonclick()