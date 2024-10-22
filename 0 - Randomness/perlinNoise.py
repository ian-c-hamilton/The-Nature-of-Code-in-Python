import py5
import numpy as np

def settings():
    global width
    global height
    width = 640
    height = 240
    py5.size(width, height)

def setup():
    global tx, ty
    tx = 0
    ty = 100
    py5.rect_mode(py5.CENTER)
    py5.background(255)


def draw():
    global tx, ty
    xn = py5.noise(tx)
    yn = py5.noise(ty)
    x = np.interp(xn, [0, 1], [0, width])
    y = np.interp(yn, [0, 1], [0, height])
    py5.ellipse(x, y, 16, 16)
    tx += 0.01
    ty += 0.01

py5.run_sketch()