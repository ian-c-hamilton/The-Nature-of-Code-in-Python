import py5

def settings():
    global width
    global height
    width = 640
    height = 240
    py5.size(width, height)

def setup():
    py5.rect_mode(py5.CENTER)
    py5.background(255)


def draw():
    x = py5.random_gaussian(320, 60)
    py5.no_stroke()
    py5.fill(0, 10)
    py5.circle(x, 120, 16)



py5.run_sketch()