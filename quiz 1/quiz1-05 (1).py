# Name: Saby Cortez
# Assignment: Quiz 1 - 05
# Due Date: September 14, 2018

# Question 1

# put your script here
students = 70
groupsize = 4
group = (students/groupsize)
bagspg = 2  #bags per group
legospg = 36  #legos per group

bags = group * bagspg
legos = legospg *group

print("For",students, "students split into",group,"groups you need",bags,"bags and",legos,"legos")
# Question 2

# put your script here
import turtle
window = turtle.Screen()
square=turtle.Turtle()
square.color("blue")
square.forward(100)
square.begin_fill()
for i in range(4):
    square.left(90)
    square.forward(100)
square.end_fill()
window.exitonclick()

