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

    # async def a_update(self):
    #     await self.a_default_update(self)

    # def update(self):
    #     self._update(self)

    # def _default_update(self, check_edges=True):
    #     # self.vel += self.accel
    #     # self.loc += self.vel
    #     sum2(self.accel._array, self.vel._array)
    #     sum2(self.vel._array, self.loc._array)
    #     self.vel.limit(10)
    #     if check_edges:
    #         self.checkEdges()

    # async def a_default_update(self, check_edges=True):
    #     self.vel += self.accel
    #     self.loc += self.vel
    #     self.vel.limit(10)
    #     if check_edges:
    #         self.loc.x %= 500
    #         self.loc.y %= 500

    def update(self):
        self.vel += self.accel
        self.loc += self.vel
        self.vel.limit(10)
        self.loc.x %= WIDTH
        self.loc.y %= HEIGHT

    def display(self):
        square(self.loc, 50, fill=(0, 1, 0, 1), stroke_weight=10)

    def checkEdges(self):
        self.loc.x %= WIDTH
        self.loc.y %= HEIGHT
