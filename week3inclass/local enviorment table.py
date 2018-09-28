# def smallestDiff (x, y, z) :
#     print('smallestDiff inputs:', x, y, z)
#     diff1 = abs(x - y)
#     diff2 = abs(y - z)
#     diff3 = abs(x - z)
#     minDiff = min(diff1, diff2, diff3)
#     print(diff1, diff2, diff3, 'return value:', minDiff)
#     return minDiff
# s = smallestDiff(32, 43, 90)
# print(s)
#
# def payAmt(price, percentOff, taxRate):
#     print('payAmt inputs:', price, percentOff, taxRate)
#     discount = price * percentOff
#     finalPrice = price - discount
#     taxAmt = finalPrice * taxRate
#     finalPrice = finalPrice + taxAmt
#     print(discount, finalPrice, taxAmt, 'return value:', finalPrice)
#     return finalPrice
# m = payAmt(25.99, 0.30, 0.0725)

# Defining Functions


# def ave3 (x, y, z) :
#     print("inputs: ", x, ",", y, ",", z)
#     n = x+y+z
#     n = n/3
#     return n
#
#
# res = ave3(2, 3.0, 4.0)
# print(res)
#
#
# def printName(x):
#     w = "Welcome to comp 123"
#     return (w, x)
# name = printName("Friend")
# print(name)

import turtle
win = turtle.Screen()
tt = turtle.Turtle()
def turtleSquare(sqTurt, sideLen):
    for i in range(4):
        tt.forward(sideLen)
        tt.left(90)

    return (sqTurt, sideLen)
turtleSquare(tt, 50)
turtleSquare(tt, 10)
turtleSquare(tt, 73)
win.exitonclick()

