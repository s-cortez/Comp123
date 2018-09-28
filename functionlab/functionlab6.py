"""This code uses 4 turtles to make 5 flowers by using circles."""

import turtle
import math

def flower(turt1, turt2, turt3, turt4, centerX, centerY):
    """This function calls the other four fucntions to draw a flower at centerX and centerY using the turtle module """
    drawFiveCircles(turt1, 50, centerX, centerY, )
    drawFiveCircles(turt2, 25, centerX, centerY, )
    drawCenterCircle(turt3, centerX, centerY - 15)
    drawBee(turt4, centerX - 2, centerY)

def drawFiveCircles( turt, radius, centerX, centerY):
    """This function creates petals using the inputs turt, radius, centerX, and centerY"""
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)
def drawCenterCircle(turt, centerX, centerY):
        turt.up()
        turt.goto(centerX, centerY)
        turt.down()
        turt.begin_fill()
        turt.circle(15)
        turt.end_fill()

def drawBee(turt, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.stamp()
win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

flower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)

flower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)

flower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)

flower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)

flower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)
win.exitonclick()