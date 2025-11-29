# Michaelynn Mendiola
# 11/28/2025
# P4LAB1
# Use turtle and loops to draw a sqaure and a triangle


# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()
win.bgcolor("lightblue")


# Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

# Code to draw the sqaure
for side in range(4):
    pen.forward(100)
    pen.left(90)
    
# Move arrow up
pen.goto(0, 100)

# While loop that executes 3 times
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    print(sides)
    sides = sides - 1

# Wait for user to close window
win.mainloop()