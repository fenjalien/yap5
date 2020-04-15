import pyglet
import __main__
import octo
import numpy as np
from pyglet import gl
# builtins.width = 360
# builtins.height = 360


def _dummy(*args, **kwargs):
    pass


def run(sketch_setup=None, sketch_draw=None, sketch_update=None):
    if sketch_draw is not None:
        draw_method = sketch_draw
    elif hasattr(__main__, 'draw'):
        draw_method = __main__.draw
    else:
        draw_method = _dummy

    if sketch_setup is not None:
        setup_method = sketch_setup
    elif hasattr(__main__, 'setup'):
        setup_method = __main__.setup
    else:
        setup_method = _dummy

    if sketch_update is not None:
        update_method = sketch_update
    elif hasattr(__main__, 'update'):
        update_method = __main__.update
    else:
        update_method = _dummy

    octo.window = pyglet.window.Window(
        width=octo.WIDTH,
        height=octo.HEIGHT,
        visible=False
    )
    octo.window.on_draw = draw_method
    pyglet.clock.schedule_interval(update_method, 1/120.0)

    setup_method()
    
    octo.window.set_visible()

    pyglet.app.run()


def size(width, height):
    octo.WIDTH = int(width)
    octo.HEIGHT = int(height)
    octo.window.set_size(octo.WIDTH, octo.HEIGHT)


def clear():
    octo.window.clear()

def background(R, G, B, A=1):
    pyglet.gl.glClearColor(R, G, B, A)
    clear()
