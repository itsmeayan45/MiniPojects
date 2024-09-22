import turtle

# Setup the window
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle named "flower"
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)  # Adjust the speed for faster drawing

# Function to draw a petal
def draw_petal():
    flower.color("red")
    flower.begin_fill()
    flower.circle(100, 60)  # Draw an arc (half petal)
    flower.left(120)
    flower.circle(100, 60)  # Draw the other arc (other half petal)
    flower.left(120)
    flower.end_fill()

# Function to draw the flower with multiple petals
def draw_flower():
    for _ in range(6):
        draw_petal()
        flower.right(60)  # Rotate to position for the next petal

# Draw flower
draw_flower()

# Draw the center of the flower
flower.color("yellow")
flower.penup()
flower.goto(0, -20)
flower.pendown()
flower.begin_fill()
flower.circle(20)  # Draw a circle for the center
flower.end_fill()

# Hide the turtle
flower.hideturtle()

# Finish
window.mainloop()