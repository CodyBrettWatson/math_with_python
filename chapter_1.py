import turtle
from turtle import *
turt = turtle.Turtle()
turt.speed(0)
turt.hideturtle()

# a = turtle.Turtle()      #instantiate a new turtle object called 'a'
# a.hideturtle()           #make the turtle invisible
# a.penup()                #don't draw when turtle moves
# a.goto(-200, -200)       #move the turtle to a location
# a.showturtle()           #make the turtle visible
# a.pendown()              #draw when the turtle moves
# a.goto(50, 50)           #move the turtle to a new location

def square():
    for i in range(4):
        right(90)
        forward(200)

def eight_point_star():
    for i in range(8):
        right(45)
        forward(200)
        right(90)

def sixty_point_star():
    for i in range(30):
        right(5)
        forward(50)
        right(90)

def imbedded_stars():
    square()
    back(142)
    eight_point_star()
    left(90)
    back(75)
    right(90)
    forward(20)
    sixty_point_star()

def square_again (sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

def layered_square():
    square_again(30)
    square_again(60)
    square_again(90)
    square_again(120)
    square_again(150)
    square_again(180)

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        left(120)

def rose_sixty_point_star(sidelength=100):
    for i in range(100):
        right(5)
        forward(sidelength)
        right(90)
        sidelength+=5

def snail_sixty_point_star(sidelength=100):
    for j in range(100):
        for i in range(4):
            forward(sidelength)
            right(90)
        right(5)
        sidelength+=5



def s_spiral_5_degrees(sidelength=100, angle=90):
    for i in range(1000):
        right(5)
        forward(sidelength)
        right(angle)
        sidelength+=.1
        angle-=5
        if angle==0:
            angle=360
    exitonclick()

def s_spiral_degrees(rangecount=1000, sidelength=100, angle=90, sidelengthchange=.1, anglechange=5):
    for i in range(rangecount):
        right(5)
        forward(sidelength)
        right(angle)
        sidelength+=sidelengthchange
        angle-=anglechange
        if angle<=0:
            angle=360
    exitonclick()

s_spiral_degrees(1000,1,360,1,180)