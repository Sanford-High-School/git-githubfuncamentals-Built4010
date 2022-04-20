# Write your code here :-)
import turtle
import random

#get ready
wn = turtle.Screen()
Jo = turtle.Turtle()

Jo.shape('circle')
Jo.shapesize(1)
Jo.penup()
Jo.speed(10)


vertex1_x = 130
vertex1_y = 100
Jo.goto(vertex1_x,vertex1_y)
Jo.stamp()



vertex2_x = -200
vertex2_y = 150
Jo.goto(vertex2_x,vertex2_y)
Jo.stamp()



vertex3_x =0
vertex3_y = -250
Jo.goto(vertex3_x,vertex3_y)
Jo.stamp()


#Jo starting point
#x = turtle.xcor()
#y = turtle.ycor()
x = 5
y = 5


def one(x,y):
    x = (vertex1_x + x)/2
    y = (vertex1_y + y)/2
    return x,y

def two(x,y):
    x = (vertex2_x + x)/2
    y = (vertex2_y + y)/2
    return x,y
def three(x,y):
    x = (vertex3_x + x)/2
    y = (vertex3_y + y)/2
    return x,y


for c in range(500):
    n = random.randint(1,3)
    print(n)

    if n == 1:
       one(x,y)
       Jo_x,Jo_y= one(x,y)
       Jo.goto(x,y)
       Jo.stamp()
    elif n == 2:
        two(x,y)
        Jo_x,Jo_y= two(x,y)
        Jo.goto(x,y)
        Jo.stamp()
    else:
        three(x,y)
        Jo_x,Jo_y= three(x,y)
        Jo.goto(x,y)
        Jo.stamp()





wn.mainloop()
