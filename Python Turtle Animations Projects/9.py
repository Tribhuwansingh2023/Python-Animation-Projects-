# Copyright (c) 2023 Tribhuwan Singh
# All rights reserved.

# This script is copyrighted under Tribhuwan Singh, 2023. 
# Unauthorized copying, distribution, or modification of this code, 
# via any medium, is strictly prohibited unless granted permission 
# by the copyright holder.
import time
from turtle import *
import colorsys
bgcolor("black")
pensize(2)
tracer(2)
time.sleep(10)

h = 0
goto(0, 0)
for x in range(500):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    fillcolor(c)
    h += 0.999
    begin_fill()
    up()
    forward(x)
    down()
    right(9)
    forward(x)
    right(100)
    right(107)
    end_fill()

hideturtle()
done()
