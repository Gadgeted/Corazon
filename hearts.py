import turtle
import math
import numpy as np

# Setup Turtle
# Setup Turtle
# Setup Turtle
# Setup Turtle
# Setup Turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

def heart_curve(n):
    """Generates x, y coordinates for a heart shape based on parametric equations."""
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

def draw_heart(scale_factor):
    """Draws a single heart shape scaled by scale_factor."""
    t.penup()
    for n in np.linspace(0, 2 * math.pi, 300):  # Smooth heart shape
        x, y = heart_curve(n)
        t.goto(x * scale_factor, y * scale_factor)
        t.pendown()

def layered_hearts(layers=15, scale_step=2):
    """Draws multiple scaled hearts for a layered effect."""
    for i in range(1, layers + 1):
        draw_heart(i * scale_step)

# Move to starting position and draw layered hearts
t.penup()
t.goto(0, 0)
t.pendown()

layered_hearts()

t.hideturtle()
turtle.done()
