import turtle

window = turtle.Screen()
star=turtle.Turtle()
red=turtle.Turtle()
star.color("blue")
star.shape("turtle")
star.pensize(3)
star.left(144)
for i in range(5):
    star.forward(60)
    star.left(144)
red.color("red")
red.shape("turtle")
red.pensize(3)
red.up()
red.forward(80)
red.down()
red.left(144)
for i in range(5):
    red.forward(60)
    red.left(144)
window.exitonclick()

