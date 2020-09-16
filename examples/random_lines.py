from yap5 import *
from random import randint
from pyglet import gl

start = Vector(0, 0)


def setup():
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    background(Color("white"))
    size(300, 300)


def draw():
    line(
        start,
        Vector(randint(0, WIDTH), HEIGHT),
        Theme(
            stroke=Color(
                randint(0, 50),
                randint(0, 255),
                randint(0, 255),
                100),
            stroke_weight=12
        )
    )
    start.x = (start.x + 1) % WIDTH


run()
