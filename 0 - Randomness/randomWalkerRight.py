import py5
import math
import random

def settings():
    global width
    global height
    width = 640
    height = 240
    py5.size(width, height)

def setup():
    global w1
    py5.rect_mode(py5.CENTER)
    py5.background(255)
    w1 = Walker(width, height)

def draw():
    w1.step()
    w1.show()

class Walker:
    def __init__(self, width, height):
        self.x = width / 2
        self.y = height / 2

    def show(self):
        py5.stroke(0)
        py5.point(self.x, self.y)

    def step(self):
        self.choice = random.random()
        if self.choice < 0.4:
            self.x += 1
        elif self.choice < 0.6:
            self.x -= 1
        elif self.choice < 0.8:
            self.y += 1
        else:
            self.y -= 1

py5.run_sketch()
