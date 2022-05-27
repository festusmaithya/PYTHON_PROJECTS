# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:41:02 2022

@author: Festus Maithya
"""

import turtle

pat=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor("black")
pat.speed(90000)

radius=70
pat.pensize(2)
colour=['red','magenta','blue']

for x in range(12):
    pat.color(colour[2])
    for i in range(6):
        pat.circle(radius)
        pat.right(60)
    radius=radius+4
turtle.done()
