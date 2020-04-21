import pyglet
import __main__
import builtins
import yap5
import numpy as np
from pyglet import gl
from .color import Color

__all__ = [
    'run',
    'size',
    'clear',
    'background'
]


builtins.WIDTH = 360
builtins.HEIGHT = 360




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

    yap5.window = pyglet.window.Window(
        width=builtins.WIDTH,
        height=builtins.HEIGHT,
        # visible=False,
        resizable=True
    )

    setup_method()
    
    yap5.window.on_draw = draw_method
    yap5.window.on_draw()
    pyglet.clock.schedule_interval(update_method, 1/120.0)
    # yap5.window.set_visible()

    pyglet.app.run()


def size(width, height):
    builtins.WIDTH = int(width)
    builtins.HEIGHT = int(height)
    yap5.window.set_size(builtins.WIDTH, builtins.HEIGHT)


def clear():
    yap5.window.clear()

def background(color: Color):
    pyglet.gl.glClearColor(*color.normalized)
    clear()
