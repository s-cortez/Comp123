# Problem 5


"""
Draw Tree

This script uses functions and loops to make a cute drawing of a tree!

Due: 9/21/18
Author: Saby Cortez
"""


# -----------------------------------------------------
# Question 5: Put your script to draw a tree here
import turtle

scr = turtle.Screen()
scr.bgcolor("skyblue")


def maketrunk(turt, x, y):
    turt.up()
    turt.goto(x, y)
    turt.down()
    for i in range(2):
        turt.begin_fill()
        turt.forward(80)
        turt.left(90)
        turt.forward(250)
        turt.end_fill()
        turt.left(90)


def makebranch(turt, x, y):
    turt.up()
    turt.goto(x, y)
    turt.down()
    turt.begin_fill()
    for i in range(2):
        turt.forward(400)
        turt.left(90)
        turt.forward(300)
        turt.left(90)
    turt.end_fill()


def makeapple(turt, x, y):
    turt.up()
    turt.goto(x, y)
    turt.down()
    turt.begin_fill()
    for i in range(5):
        for ii in range(4):
            turt.forward(30)
            turt.left(90)
        turt.up()
        turt.forward(80)
        turt.down()
    turt.end_fill()


trunk = turtle.Turtle()
trunk.color("darkgoldenrod")

branch = turtle.Turtle()
branch.color("darkolivegreen")

apple = turtle.Turtle()
apple.color("crimson")


maketrunk(trunk, -40, -300)
makebranch(branch, -200, -50)
makeapple(apple, -175, 0)
makeapple(apple, -175, 80)
makeapple(apple, -175, 160)

bird = turtle.Turtle()
bird.color("forestgreen")
bird.shape("turtle")
bird.up()
bird.goto(20, -200)
bird.left(90)
bird.down()
bird.stamp()
scr.exitonclick()
