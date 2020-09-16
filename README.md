# "Yet Another P5"
A rewrite of p5py/p5 that focuses more on the 2D side of drawing and is built on pyglet.

Functions that change global drawing state are gone, instead pass a Theme object to each drawing function. There are defaults.

There are the standard processing style `setup` and `draw` functions. `draw` is set to be the `on_draw` method of the `pyglet` window. However there is an additional `update` function that is passed a `dt` variable.
So: 

- `setup`: variable/value creation
- `draw`: Only call draw functions, don't change variables such as position.
- `update`: Update variables such as position, don't draw

Finally as its built on pyglet you can still run pyglet functions, and the main window is in the variable `window`.

Its going to be a while before I can sit down and write any coherent documentation, so if you get stuck try and read through the code otherwise raise an issue.

## Install
Clone the directory and run `pip install .`.