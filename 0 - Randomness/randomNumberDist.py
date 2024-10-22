import py5
import math
import random
import numpy as np

def settings():
    global width, height
    width = 640
    height = 240
    py5.size(width, height)

def setup():
    global total
    global randomCounts
    total = 20
    randomCounts = [0] * total


def draw():
    py5.background(255)
    index = random.randint(0, len(randomCounts) - 1)
    randomCounts[index] += 1

    py5.stroke(0)
    py5.fill(127)
    w = width / len(randomCounts)
    for x in range(len(randomCounts)):
        py5.rect(x * w, height - randomCounts[x], w - 1, randomCounts[x])


py5.run_sketch()
