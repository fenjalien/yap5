import numpy as np
import pyglet
from pyglet import gl


n_vertices = 50
angles = (np.arange(n_vertices) * 2 * np.pi / n_vertices)
unit_circle = np.array([np.cos(angles), np.sin(angles)]).T


def circle(center, radius, fill=None, stroke=(0, 0, 0, 1), stroke_weight=1, draw=True):
    vertices = (unit_circle * radius + center).reshape(1, n_vertices*2)[0]
    batch = pyglet.graphics.Batch()
    if fill:

        batch.add(n_vertices, pyglet.gl.GL_TRIANGLE_FAN, pyglet.graphics.Group(),
                  ('v2f', vertices), ('c4f', n_vertices*fill))
    if stroke:
        pyglet.gl.glLineWidth(float(stroke_weight))
        gl.glPointSize(stroke_weight)
        batch.add(n_vertices, pyglet.gl.GL_LINE_LOOP, None,
                  ('v2f', vertices), ('c4f', n_vertices*stroke))
        batch.add(n_vertices, gl.GL_POINTS, None,
                  ('v2f', vertices), ('c4f', n_vertices*stroke))
    if not draw:
        return batch
    batch.draw()
