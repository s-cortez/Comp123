# Name: Saby Cortez
# Assignment: Quiz 2
# Due Date: September 28, 2018

import turtle

# Put your function definition for drawArm here
def drawArm(turt, length, angle):
    turt.forward(length)
    turt.backward(length/2)
    turt.left(angle)
    turt.forward(length/2)
    turt.backward(length/2)
    turt.right(angle)#
    turt.right(angle)
    turt.forward(length/2)
    turt.backward(length/2)
    turt.left(angle)#
    turt.backward(length/2)


# Put your function definition for drawArm here
def drawSnowflake(turt, length, angle):
    for i in range(6):
        turt.right(60)
        drawArm(turt,length, angle)

# the script below tests the drawArm function

# scr = turtle.Screen()
# tt = turtle.Turtle()
# tt.pensize(10)
#
# drawArm(tt, 100, 40)
#
# tt.up()
# tt.goto(-100,100)
# tt.left(60)
# tt.down()
#
# drawArm(tt, 200, 30)
#
# scr.exitonclick()
'''

# The script below tests the drawSnowflake function
'''
windw = turtle.Screen()
ruddi = turtle.Turtle()
ruddi.pensize(10)

ruddi.color('red')
ruddi.up()
ruddi.goto(-250, 200)
ruddi.down()

drawSnowflake(ruddi, 100, 40)

ruddi.color('blue')
ruddi.up()
ruddi.goto(250, -100)
ruddi.down()

drawSnowflake(ruddi, 200, 50)

ruddi.color('green')
ruddi.up()
ruddi.goto(0, 0)
ruddi.down()

drawSnowflake(ruddi, 50, 30)

windw.exitonclick()
