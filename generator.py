import math
import time
import random
import tkinter as tkinter
from tkinter import *

root = Tk()
root.title("World")

#continent/land clustering -- if previous tile was land, next tile more likely to be land?

tilemap = []
max_temp = 0.0
cold = 0.05
isWater = 0.55
size = 50

class tile():
    def __init__(self, color, xcor, ycor, temp, isWater):
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        self.temp = temp
        self.isWater = isWater

        if self.temp < (cold*max_temp): #if too cold, will be icy
            self.color = 'white'
        if (cold*max_temp) <= self.temp:
            a = random.uniform(0.0, 1.0) #if warm enough to be not ice, chance to be water vs land
            if a < isWater:
                self.color = 'blue'
            else:
                self.color = 'green'


def generate_new(a):
    global max_temp

    for x in range(a):
        for y in range(a):
            
            if y >= (0.5*float(a)): #cold near poles
                t = random.uniform(0, float((a-y)/a)) #decimal between 0[near edge] and 1[near center]
            else:
                t = random.uniform(0, float(y/a)) #decimal between 0[near edge] and 1[near center]
            if t > max_temp:
                max_temp = t
            
            test = tile('red',x,y,t,isWater) #errors result in red tiles
            tilemap.append(test)

generate_new(size)

for i in tilemap:
    tkinter.Label(width=2, bg=i.color).grid(row=i.ycor,column=i.xcor)
root.mainloop()