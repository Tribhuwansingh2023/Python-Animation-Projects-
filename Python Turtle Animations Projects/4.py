# Copyright (c) 2023 Tribhuwan Singh
# All rights reserved.

# This script is copyrighted under Tribhuwan Singh, 2023. 
# Unauthorized copying, distribution, or modification of this code, 
# via any medium, is strictly prohibited unless granted permission 
# by the copyright holder.

import math
from turtle import *
pensize(2)

def heart(k):
    return 15* math.sin(k)**3
def heart1(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(0)
bgcolor('white')

for i in range(600):
    goto(heart(i)*20,heart1(i)*20)
    for j in range(5):
        color('red')
done()
