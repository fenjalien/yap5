import numpy as np
import pyglet
from pyglet import gl
from .vectors import Vector
from typing import List
from .octo import CORNER, CENTER, RADIUS


def vectors2vertices(vs: List[Vector]):
    vertices = []
    for v in vs:
        vertices.extend(v._array.tolist())
    return vertices


def polygon(vertices: List[Vector], fill=None, stroke=(0, 0, 0, 1), stroke_weight=1):
    # batch = pyglet.graphics.Batch()
    n_vertices = len(vertices)
    vertices = vectors2vertices(vertices)
    if fill:
        gl.glPolygonMode(gl.GL_FRONT, gl.GL_FILL)
        pyglet.graphics.draw(n_vertices, gl.GL_POLYGON,
                  ('v2f', vertices), ('c4f', n_vertices*fill))
    if stroke:
        gl.glLineWidth(float(stroke_weight))
        gl.glPolygonMode(gl.GL_FRONT, gl.GL_LINE)
        pyglet.graphics.draw(n_vertices, gl.GL_POLYGON,
                  ('v2f', vertices), ('c4f', n_vertices*stroke))
        gl.glPolygonMode(gl.GL_FRONT, gl.GL_POINT)
        gl.glPointSize(float(stroke_weight))
        pyglet.graphics.draw(n_vertices, gl.GL_POLYGON,
                  ('v2f', vertices), ('c4f', n_vertices*stroke))



circle_n_vertices = 50
circle_angles = (np.arange(circle_n_vertices) * 2 * np.pi / circle_n_vertices)
unit_circle = np.array([Vector.from_angle(a) for a in circle_angles])


def circle(coordinate, radius, fill=None, stroke=(0, 0, 0, 1), stroke_weight=1, draw=True):
    vertices = (unit_circle * radius) + coordinate
    polygon(vertices=vertices, fill=fill, stroke=stroke, stroke_weight=stroke_weight)


unit_square = np.array([Vector.from_angle(a) for a in (np.arange(4) * np.pi / 2 + np.pi / 4)])

def square(coordinate, side_length, mode=CENTER, fill=None, stroke=(0, 0, 0, 1), stroke_weight=1):
    if mode is CENTER:
        vertices = unit_square * side_length + coordinate
    elif mode is CORNER:
        vertices = unit_square * side_length + coordinate + Vector(side_length/2, side_length/2)
    elif mode is RADIUS:
        vertices = unit_square * (side_length / 2) + coordinate + Vector(side_length/2, side_length/2)
    else:
        raise ValueError
    polygon(vertices=vertices, fill=fill, stroke=stroke, stroke_weight=stroke_weight)
