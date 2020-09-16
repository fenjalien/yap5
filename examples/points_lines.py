from yap5 import *

d = 70
p1 = d
p2 = p1 + d 
p3 = p2 + d
p4 = p3 + d


box = Theme(stroke=Color('white'))
pts = Theme(stroke=Color('gray'))

def setup():
    size(640, 360)

def draw():
    background(Color('black'))
    square(Vector(p3, p3), d, mode=CORNER, theme=box)

    points(
        [
            Vector(p1, p1),
            Vector(p1, p3),
            Vector(p2, p4),
            Vector(p3, p1),
            Vector(p4, p2),
            Vector(p4, p4),
        ],
        pts
    )

run()