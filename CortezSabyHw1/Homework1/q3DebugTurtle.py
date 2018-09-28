# Problem 3


"""
Debug Turtle

This script draws uses the turtle and math modules
to draw a blue triangle with a green circle inscribed in it and a
brown line running through the center.

Due:9/21/18
Author: <Saby Cortez>
"""

import turtle
import math

# -----------------------------------------------------
# Question 3: Find four bugs in the script below


"""This script draws a blue triangle with a green circle inside it,
 bisected by a brown line."""

scr = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)


scr.bgcolor("whitesmoke")

turt.up()
turt.right(90)
turt.forward(200)
turt.left(90)
turt.down()

turt.color("steelblue")
turt.begin_fill()
turt.forward(200)
turt.left(120)
turt.forward(400)
turt.left(120)
turt.forward(400)
turt.left(120)
turt.forward(200)
turt.end_fill()  # There was no ()

turt.color("forestgreen")
radius = 200 / math.sqrt(3)  # Forgot "math." before sqrt()
turt.begin_fill()
turt.circle(radius)  # Typed turtle instead of turt
turt.end_fill()

turt.color("saddlebrown")
turt.pensize(5)
turt.left(90)  # Misspelled left
height = 200 * math.sqrt(3)
turt.forward(height)

# This line is just so you can see the turtle at the end
turt.color('black')

scr.exitonclick()
