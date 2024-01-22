import turtle
import math

# Create a turtle screen (canvas)
screen = turtle.Screen()

# Create a turtle
bob = turtle.Turtle()

# Move the turtle to some coordinates (example)
# bob.pu()
# bob.fd(100)
# bob.rt(90)
# bob.fd(100)
# bob.rt(90)
# bob.pd()
# bob.fd(100)
# bob.rt(90)
# bob.fd(100)

# screen.exitonclick()

for i in range(4):
    print('Hello')

# for i in range(4):
#     bob.fd(150)
#     bob.lt(90)

def square(t, len):
    for i in range(4):
        t.fd(len)
        t.lt(90)

# square(bob, 10)
        
def polygon(t, len, n):
    angle = 360/n
    for i in range(n):
        t.fd(len)
        t.lt(angle)

# polygon(t = bob, len = 100, n = 8)
        
def circle(t, r):
    circumference = 2 * math.pi * r
    degrees = 360
    for i in range(degrees):
        t.lt(1)
        t.fd(circumference / degrees)

# circle(bob, 150)
        
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# arc(bob, 50, 720)
        
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)