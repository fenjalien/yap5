import pyglet
import __main__
import builtins
import octo

builtins.width = 360
builtins.height = 360


def _dummy(*args, **kwargs):
    pass


def run(sketch_setup=None, sketch_draw=None, sketch_update=None):
    if sketch_draw is not None:
        draw_method = sketch_draw
    # elif hasattr(__main__, 'draw'):
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

    
    octo.window = pyglet.window.Window(width=builtins.width, height=builtins.height)
    octo.window.on_draw = draw_method
    pyglet.clock.schedule_interval(update_method, 1/120.0)
    
    setup_method()

    pyglet.app.run()


def size(width, height):
    builtins.width = int(width)
    builtins.height = int(height)
    octo.window.set_size(builtins.width, builtins.height)


def clear():
    octo.window.clear()

def background(R, G, B, A=1):
    pyglet.gl.glClearColor(R, G, B, A)
    clear()