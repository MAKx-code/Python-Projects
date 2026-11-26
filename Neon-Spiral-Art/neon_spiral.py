
import turtle

# Create the drawing window
screen = turtle.Screen()
screen.bgcolor("#080812")
screen.title("MAKx - Neon Spiral Art")

# Create the drawing pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Neon colour palette
colors = [
    "#FF00FF",
    "#00FFFF",
    "#7B2CFF",
    "#FF1493",
    "#00FF99",
    "#FFFFFF"
]

# Draw the spiral
for i in range(180):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 1.5)
    pen.right(121)

# Keep the window open
turtle.done()
