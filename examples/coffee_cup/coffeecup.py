from yap5 import *
import numpy as np


class CoffeCup(object):
    center: Vector
    radius: float

    n_points: int
    table: float

    points: [Vector]

    def __init__(self, center=Vector(0, 0), num_of_points=100, times_table=2, radius=100):
        self.center = center
        self.n_points = num_of_points
        self.table = times_table
        self.radius = radius
        self.points = []

    def calc_points(self):
        self.points = []
        angle = np.pi * 2 / self.n_points
        for p in range(self.n_points):
            self.points.append(
                Vector(
                    self.center.x + np.cos(angle*p)*self.radius,
                    self.center.y + np.sin(angle*p)*self.radius,
                )
            )

    def draw(self):
        if self.n_points != len(self.points):
            self.calc_points()

        line_coordinates = []
        for start in range(self.n_points):
            line_coordinates.append(self.points[start])
            line_coordinates.append(
                self.points[
                    int(start*self.table) % self.n_points
                ]
            )
        lines(line_coordinates)
