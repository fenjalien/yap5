import numpy as np
from typing import Union

EPSILON = 1e-8


def isnumeric(obj):
    return isinstance(obj, int) or isinstance(obj, float)


class Vector(object):
    def __init__(self, x, y):
        self._array = np.array([x, y], dtype=np.float32)

    @property
    def x(self):
        return self._array[0]

    @x.setter
    def x(self, value: float):
        self._array[0] = value

    @property
    def y(self):
        return self._array[1]

    @y.setter
    def y(self, value: float):
        return self._array[1]

    def __add__(self, other: 'Vector'):
        return self.__class__(*(self._array + other._array))

    def __sub__(self, other: 'Vector'):
        return self.__class__(*(self._array - other._array))

    def __mul__(self, other: Union[int, float]):
        if isnumeric(other):
            return self.__class__(*(other * self._array))
        raise TypeError

    def __rmul__(self, other: Union[int, float]):
        return self * other

    def __neg__(self):
        return (-1) * self

    def __div__(self, other: Union[int, float]):
        if isnumeric(other):
            return self * (1 / other)
        raise TypeError

    def __abs__(self):
        return self.magnitude

    def __getitem__(self, key):
        return self._array[key]

    def __setitem__(self, key, value):
        self._array[key] = value

    def __iter__(self):
        for k in self._array:
            yield k

    def __eq__(self, other: 'Vector'):
        if hasattr(other, '_array') and self._array.shape == other._array.shape:
            return np.all(np.abs(self._array - other._array) < EPSILON)
        return False

    def __neq__(self, other: 'Vector'):
        if hasattr(other, '_array') and self._array.shape == other._array.shape:
            return not np.all(np.abs(self._array - other._array) < EPSILON)
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    __str__ = __repr__

    def cross(self, other: 'Vector'):
        return self.__class__(*(np.cross(self._array, other._array)))

    def dot(self, other: 'Vector'):
        return self.__class__(*(np.dot(self._array, other._array)))

    def distance(self, other: 'Vector'):
        return np.sqrt(np.sum(self._array - other._array)**2)

    dist = distance

    @property
    def angle(self):
        return np.arctan2(self.y, self.x)

    @angle.setter
    def angle(self, theta: Union[int, float]):
        self.rotate(theta - self.angle)

    def rotate(self, theta: Union[int, float]):
        self._array = np.array([
            self.x * np.cos(theta) - self.y * np.sin(theta),
            self.x * np.sin(theta) + self.y * np.cos(theta),
        ],
            dtype=np.float32)

    def angle_between(self, other: 'Vector'):
        return np.arccos((self.dot(other)) /
                         (self.magnitude * other.magnitude))

    @property
    def magnitude_sq(self):
        return np.dot(self._array, self._array)

    @magnitude_sq.setter
    def magnitude_sq(self, value):
        self.magnitude = np.sqrt(value)

    @property
    def magnitude(self):
        return np.sqrt(self.magnitude_sq)

    @magnitude.setter
    def magnitude(self, value):
        self._array = (value * self._array) / self.magnitude

    def normalize(self):
        self.magnitude = 1
        return self

    def limit(self, upper_limit=None, lower_limit=None):
        magnitude = self.magnitude
        if upper_limit is None:
            upper_limit = magnitude
        if lower_limit is None:
            lower_limit = magnitude

        if magnitude < lower_limit:
            self.magnitude = lower_limit
        elif magnitude > upper_limit:
            self.magnitude = upper_limit

    def copy(self):
        return self.__class__(*self._array)