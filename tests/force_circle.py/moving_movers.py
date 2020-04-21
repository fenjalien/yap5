import sys
sys.path.append('D:/code/octo')
from movers import Mover
from yap5 import *


# m = Mover()
ms = []
gravity = Vector(0, -0.1)
wind = Vector(0.01, 0)


def setup():
    size(640, 360)

    for m in range(10):
        ms.append(Mover(Vector(10, HEIGHT-10), m+1))


def draw():
    background(Color('white'))

    for m in ms:
        m.draw()


def update(dt):
    for m in ms:
        m.applyForce(wind)
        m.applyForce(gravity)
        m.update()


if __name__ == "__main__":
    run()
