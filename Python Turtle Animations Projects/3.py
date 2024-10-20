# Copyright (c) 2023 Tribhuwan Singh
# All rights reserved.

# This script is copyrighted under Tribhuwan Singh, 2023. 
# Unauthorized copying, distribution, or modification of this code, 
# via any medium, is strictly prohibited unless granted permission 
# by the copyright holder.

from turtle import *
import colorsys as cs

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1.0, height=1.0)
pensize(2)
shape('turtle')
N = 18
color(cs.hsv_to_rgb((N-3)/20,1,1))
A = 360/N
for i in range(N):
    for j in range(N):
        fd(100-N*3)
        rt(A)
    rt(A)
    
done()