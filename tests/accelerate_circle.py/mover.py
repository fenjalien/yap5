from p5 import random_uniform, noise, constrain
from octo import *
from typing import Callable
import numpy as np

boundary = np.array([600, 600, 1])


class Mover(object):
    loc: Vector  # Location
    vel: Vector  # Velocity
    accel: Vector  # Acceleration
    # The '' is for a forward decleration of Mover
    _update: Callable[['Mover'], None]

    def __init__(self, location: Vector, velocity: Vector, acceleration: Vector, update_=None):
        # self._update = self._default_update if update_ is None else update_
        self.loc = location
        self.vel = velocity
        self.accel = acceleration
        self.theme = Theme(fill=Color('green'), stroke_weight=10)

    @classmethod
    def fromRandom(cls):
        return cls(
            Vector(random_uniform(WIDTH), random_uniform(HEIGHT)),
            Vector(random_uniform(2, -2), random_uniform(2, -2)),
            Vector(random_uniform(0.01, -0.01), random_uniform(0.01, -0.01))
        )

    @classmethod
    def withRandomAcceleration(cls):
        def update(self: 'Mover'):
            self.accel = Vector.random_2D() * noise(*self.loc)
            self._default_update()
        return cls(
            Vector(random_uniform(WIDTH), random_uniform(HEIGHT)),
            Vector(random_uniform(2, -2), random_uniform(2, -2)),
            Vector(0, 0),
            update_=update
        )

    @classmethod
    def followMouse(cls):
        def update(self: 'Mover'):
            self.accel = (Vector(mouse_x, mouse_y) -
                          self.loc).normalize() * 0.5
            self._default_update(check_edges=False)
            self.loc.x = constrain(self.loc.x, 0, WIDTH)
            self.loc.y = constrain(self.loc.y, 0, HEIGHT)
        return cls(
            Vector(random_uniform(WIDTH), random_uniform(HEIGHT)),
            Vector(random_uniform(2, -2), random_uniform(2, -2)),
            Vector(0, 0),
            update_=update
        )

    def update(self):
        self.vel += self.accel
        self.loc += self.vel
        self.vel.limit(10)
        self.loc.x %= WIDTH
        self.loc.y %= HEIGHT

    def display(self):
        circle(self.loc, 50, theme=self.theme)

    def checkEdges(self):
        self.loc.x %= WIDTH
        self.loc.y %= HEIGHT
