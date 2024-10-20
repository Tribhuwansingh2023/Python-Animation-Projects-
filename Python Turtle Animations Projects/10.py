# Copyright (c) 2023 Tribhuwan Singh
# All rights reserved.

# This script is copyrighted under Tribhuwan Singh, 2023. 
# Unauthorized copying, distribution, or modification of this code, 
# via any medium, is strictly prohibited unless granted permission 
# by the copyright holder.
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# set the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.bgcolor("Green")
wn.tracer(0) 

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.color("Black")
head.shape("square")
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 High Score: 0', align='center', font=("Courier", 24, 'normal'))


# functions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


# keyboard binding
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, "Right")

while True:
    wn.update()

    # check  for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f'Score: {score} High Score: {high_score}', align='center', font=("Courier", 24, 'normal'))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    time.sleep(delay)
    move()

    # Check for head collision with the body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segment list
            segments.clear()

            # Reset the score
            score = 0

            # Update the score display
            pen.clear()
            pen.write(f'Score: {score} High Score: {high_score}', align='center', font=("Courier", 24, 'normal'))

wn.mainloop()