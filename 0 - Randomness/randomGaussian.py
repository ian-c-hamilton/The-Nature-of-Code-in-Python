import py5

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


def draw():
    w1.step()
    w1.show()

py5.run_sketch()