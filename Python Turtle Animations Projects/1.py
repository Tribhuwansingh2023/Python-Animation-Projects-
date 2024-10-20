# Copyright (c) 2023 Tribhuwan Singh
# All rights reserved.

# This script is copyrighted under Tribhuwan Singh, 2023. 
# Unauthorized copying, distribution, or modification of this code, 
# via any medium, is strictly prohibited unless granted permission 
# by the copyright holder.


from turtle import*
from colorsys import*
tracer(5)
bgcolor('black')
pensize(4)
h=0.4
up()
goto(-260, -200)
down()
for i in range(700):
	c = hsv_to_rgb(h,1,1)
	h += 0.005
	color(c)
	begin_fill()
	fd(i)
	rt(91)
	up()
	circle(250-i,90)
	down()
	circle(250-i,90)
	end_fill()
done()