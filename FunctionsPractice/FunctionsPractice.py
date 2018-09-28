"""Nested squares: this function makes a cool nested square"""
import turtle

def nestedSquares (turt):
    for i in range(10,80,10):
        for j in range (4):
            turt.forward(i)
            turt.left(90)

win = turtle.Screen()
tt = turtle.Turtle()
tt.speed(0)
nestedSquares(tt)
win.exitonclick()

"SumRange"
def sumRange(startVal, endVal):
    cnt = 0 # initialize accumulator to default value 0
    for x in range(startVal, endVal + 1):
        cnt = cnt + x # update: add new x value to old value of cnt
    return cnt


print (sumRange(1,10))  #I didn't know what to expect, got 55 because it ads up each variable from the first till the last that you call for
print(sumRange(1,1))  #I thought it would be 2, it came out as 1
print(sumRange(2,1))  #I thought it would be 0, it came out as 0
print(sumRange(-1,-3))  # I thought it would be -2 it came out as 0

"""Copystring: This question copys the string you put in and returns a cool stairs thing"""
def copyStr(string, numTimes):
    ansStr = "" # initialize accumulator to empty string
    print(ansStr)
    for x in range(numTimes):
        ansStr = ansStr + string # update ansStr
        print(ansStr)
    return ansStr


print(copyStr("hi", 6))

"""String of Numbers"""
def stringOfNums(number):
    ansstr = ""
    for x in range(1, number + 1):
        ansstr += str(x) + " "
    print(ansstr)


stringOfNums(10)
"""Roof stuff"""
import math


def rectArea(length, width):
    area = length * width
    return math.ceil(area)


def roofCost(length, width, price):
    return rectArea(length, width) * price


print(roofCost(10, 10, 10))


"""Optional"""
def mpTable(small, big):
    for i in range(small, big+1):
        rn = ""
        for j in range(small, big+1):
            rn += str(i*j) + " "
        print(rn)

mpTable(1,5)