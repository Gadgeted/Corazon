import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
#background color goes here
# color can change
turtle.bgcolor("black")

def corazon(n):
    """Generates x, y coordinates for a heart shape"""
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2*math.cos(3*n) - math.cos(4*n)
    return x, y

# Move to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw multiple hearts for a layered effect
for i in range(1, 15):  # Increasing effect with scale
    scale = i * 2  # Scale factor to grow the heart
    t.penup()
    
    for n in range(0, 628, 2):  # Looping from 0 to 2π (~6.28 radians)
        angle = n / 100  # Convert to radians
        x, y = corazon(angle)
        t.goto(x * scale, y * scale)
        t.pendown()

t.hideturtle()
turtle.done()