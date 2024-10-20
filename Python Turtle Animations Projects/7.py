# Copyright (c) 2023 Tribhuwan Singh
# All rights reserved.

# This script is copyrighted under Tribhuwan Singh, 2023. 
# Unauthorized copying, distribution, or modification of this code, 
# via any medium, is strictly prohibited unless granted permission 
# by the copyright holder.

import turtle
screen = turtle.Screen()
screen.bgcolor("black")
turtle.speed(10)
turtle.pensize(2)
turtle.goto(0, 0) 
import time

time.sleep(5)
def draw_spiral(n, l, a, c):
    for _ in range(n):
        turtle.color(c, 1, 1)
        for _ in range(360):
            turtle.forward(l)
            turtle.right(a)
            c = (c +  0.005) % 1

n = 100
l = 400
a = 91
c = 0.0

draw_spiral(n, l, a, c)
