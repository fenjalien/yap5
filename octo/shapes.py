import numpy as np
import pyglet
from pyglet import gl
from .pmath import Vector
from typing import List
from .constants import CORNER, CENTER, RADIUS, CORNERS
from .theme import Theme


__all__ = [
    'polygon',
    'circle',
    'square',
    'rectangle',
    'point'
]


def vectors2vertices(vs: List[Vector]):
    vertices = []
    for v in vs:
        vertices.extend(v._array.tolist())
    return vertices


def polygon(vertices: List[Vector], theme=Theme()):
    # batch = pyglet.graphics.Batch()
    n_vertices = len(vertices)
    vertices = vectors2vertices(vertices)
    if theme.fill:
        gl.glPolygonMode(gl.GL_FRONT, gl.GL_FILL)
        pyglet.graphics.draw(n_vertices, gl.GL_POLYGON,
                             ('v2f', vertices),
                             ('c4f', n_vertices*theme.fill.normalized))
    if theme.stroke:
        gl.glLineWidth(float(theme.stroke_weight))
        gl.glPolygonMode(gl.GL_FRONT, gl.GL_LINE)
        pyglet.graphics.draw(n_vertices, gl.GL_POLYGON,
                             ('v2f', vertices),
                             ('c4f', n_vertices*theme.stroke.normalized))

        gl.glPolygonMode(gl.GL_FRONT, gl.GL_POINT)
        gl.glPointSize(float(theme.stroke_weight))
        pyglet.graphics.draw(n_vertices, gl.GL_POLYGON,
                             ('v2f', vertices),
                             ('c4f', n_vertices*theme.stroke.normalized))


def point(coordinate, theme=Theme(stroke_weight=1)):
    gl.glPointSize(theme.stroke_weight)
    pyglet.graphics.draw(1, gl.GL_POINTS,
                         ('v2f', coordinate._array),
                         ('c4f', theme.stroke.normalized))


circle_n_vertices = 50
circle_angles = (np.arange(circle_n_vertices) * 2 * np.pi / circle_n_vertices)
unit_circle = np.array([Vector.from_angle(a) for a in circle_angles])


def circle(coordinate, radius, theme=Theme()):
    vertices = (unit_circle * radius) + coordinate
    polygon(
        vertices=vertices,
        theme=theme
    )


def rectangle(coordinate: Vector, *args, mode=CORNER, theme=Theme()):
    assert mode in [CORNER, RADIUS, CENTER, CORNERS]
    if mode is CORNERS:
        other = args[0]
        vertices = [
            coordinate,
            Vector(other.x, coordinate.y),
            other,
            Vector(coordinate.x, other.y),
        ]
    else:
        w, h = args
        if mode is CORNER:
            vertices = [
                coordinate,
                Vector(coordinate.x + w, coordinate.y),
                Vector(coordinate.x + w, coordinate.y + h),
                Vector(coordinate.x, coordinate.y + h)
            ]
        if mode is CENTER:
            w /= 2
            h /= 2
        if mode in [CENTER, RADIUS]:
            vertices = [
                Vector(coordinate.x - w, coordinate.y - h),
                Vector(coordinate.x + w, coordinate.y - h),
                Vector(coordinate.x + w, coordinate.y + h),
                Vector(coordinate.x - w, coordinate.y + h),
            ]
    polygon(
        vertices=vertices,
        theme=theme
    )


def square(coordinate, side_length, mode=CENTER, theme=Theme()):
    assert mode in [CORNER, CENTER, RADIUS]
    rectangle(coordinate, side_length, side_length, mode=mode, theme=theme)
