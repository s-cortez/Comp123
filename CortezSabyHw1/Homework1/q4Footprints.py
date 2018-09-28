# Problem 4


"""
Footprints

This script uses turtle stamps and loops to make footprints appear across the screen.

Due: 9/21/18
Author: <Saby Cortez>
"""


import turtle
import time

# -----------------------------------------------------
# Question 4: Complete this script to animate footprints here

scr = turtle.Screen()
scr.register_shape("leftFoot.gif")
scr.register_shape("rightFoot.gif")

leftTurt = turtle.Turtle()
leftTurt.hideturtle()
leftTurt.shape("leftFoot.gif")
leftTurt.left(90)
leftTurt.up()
leftTurt.goto(-20, -300)

rightTurt = turtle.Turtle()
rightTurt.hideturtle()
rightTurt.shape("rightFoot.gif")
rightTurt.left(90)
rightTurt.up()
rightTurt.goto(20, -350)

for i in range(8):
    time.sleep(0.7)
    rightTurt.stamp()
    rightTurt.forward(100)
    time.sleep(0.7)
    leftTurt.stamp()
    leftTurt.forward(100)

# This should be the last statement in the script
scr.exitonclick()
