from octo import Vector, circle, Theme, Color


class Mover(object):
    pos: Vector
    vel: Vector
    accel: Vector
    mass: float
    theme: Theme

    def __init__(self, position: Vector, mass: float):
        self.pos = position  # Vector(50, 150)
        self.vel = Vector(0, 0)
        self.accel = Vector(0, 0)
        self.mass = mass
        self.theme = Theme(fill=Color('gray'),stroke_weight=3)

    def update(self):
        self.vel += self.accel
        self.pos += self.vel
        self.accel *= 0
        self.vel.limit(10)
        self.checkEdges()

    def checkEdges(self):
        # self.pos.x %= WIDTH
        # self.pos.y %= HEIGHT
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
            self.vel.x *= -1
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel.x *= -1

        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
            self.vel.y *= -1

        if self.pos.y < 0:
            self.pos.y = 0
            self.vel.y *= -1

    def draw(self):
        circle(self.pos, 1.6*self.mass, theme=self.theme)

    def applyForce(self, force: Vector):
        self.accel += force / self.mass
