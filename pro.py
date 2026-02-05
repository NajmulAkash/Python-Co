from turtle import *
import math 
from colorsys import *

bgcolor('black')
hideturtle()
tracer(10)
pensize(1)

points = []
for i in range(700):
    ang = (i / 700) * 2 * math.pi
    x = 250 * math.cos(ang)
    y = 250 * math.sin(ang)
    points.append((x,y))

for i in range(700):
    j = (i * 2 ) % 700
    color(hsv_to_rgb (i / 700 , 1 , 1))
    up()
    goto(points[i])
    down()
    goto(points[j])
    done()
