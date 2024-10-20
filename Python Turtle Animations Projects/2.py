import turtle
window = turtle.Screen()
t = turtle. Turtle()
t.speed(0) 
t.pensize(2)
def spiral(size, angle):
    for _ in range(150):
        t.forward(size)
        t.right(angle)
        size += 5
def show_copyright():
    t.penup()
    t.goto(-650, -320) 
    t.pendown()
    t.hideturtle()
    t.write("© 2023 Tribhuwan Singh. All rights reserved.", align="left", font=("Arial", 12, "normal"))

spiral(0.01, 140)
show_copyright()
window.exitonclick()