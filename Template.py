import py5

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))

py5.run_sketch()