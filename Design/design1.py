import turtle


window = turtle.Screen()
window.bgcolor("black")


flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(0) 


def draw_petal(size, angle):
    flower.color("blue", "purple") 
    flower.begin_fill()
    for _ in range(2):
        flower.circle(size, angle)  
        flower.left(180 - angle)
    flower.end_fill()

def draw_flower(petals, size, angle):
    for _ in range(petals):
        draw_petal(size, angle)
        flower.left(360 / petals)  

def draw_flower_pattern(layers, petals, size, angle, gap):
    for layer in range(layers):
        draw_flower(petals, size - layer * gap, angle)
        flower.right(360 / layers)  

draw_flower_pattern(layers=6, petals=12, size=100, angle=60, gap=15)

flower.color("yellow")
flower.penup()
flower.goto(0, -20)
flower.pendown()
flower.begin_fill()
flower.circle(30)  
flower.end_fill()


flower.hideturtle()

window.mainloop()