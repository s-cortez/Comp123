import turtle
window = turtle.Screen()
friend = turtle.Turtle()
friend.color("springgreen3")
friend.pensize(3)
friend.shape("turtle")
friend.left(120)
friend.begin_fill()
for i in range(3):
    friend.forward(250)
    friend.left(120)
friend.end_fill()

window.exitonclick()