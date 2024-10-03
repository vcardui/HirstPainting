import random
from turtle import Turtle, Screen
import colorgram

colors = colorgram.extract('dots.png', 12)

color_palette = []

for item in colors:
    new_color = (item.rgb.r, item.rgb.g, item.rgb.b)
    color_palette.append(new_color)

#color_palette = [(239, 239, 239), (233, 237, 233), (233, 236, 239), (241, 234, 237), (47, 102, 166), (233, 205, 120), (226, 151, 93), (190, 45, 72), (213, 60, 76), (228, 120, 146), (114, 90, 52), (115, 108, 184)]

# Tim
tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine3")
tim.speed(10)
tim.penup()
tim.setposition(-200, -200)
tim.hideturtle()

# Screen
screen = Screen()
screen.colormode(255)


# Drawing

def hirstDots(size, space):
    for j in range(0, size):
        tim.setposition(-200, (-200 + (j * space)))

        for i in range(0, size):
            tim.dot(20, random.choice(color_palette))
            tim.forward(space)


hirstDots(10, 50)

screen.exitonclick()
