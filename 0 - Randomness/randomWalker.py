import py5
import math

def settings():
    global width
    global height
    width = 800
    height = 800
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
        self.xstep = math.floor(py5.random_int(2)) - 1
        self.ystep = math.floor(py5.random_int(2)) - 1
        self.x += self.xstep
        self.y += self.ystep
"""        if self.choice == 0:
            self.x += 1
        elif self.choice == 1:
            self.x -= 1
        elif self.choice == 2:
            self.y += 1
        elif self.choice == 3:
            self.y -= 1"""

py5.run_sketch()
