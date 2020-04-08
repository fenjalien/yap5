import sys
sys.path.append('D:/code/octo')
from octo import *
from mover import Mover

# m = Mover(Vector(width/2, height/2), Vector(0,0), Vector(0,0))
m = Mover.fromRandom()

def setup():
    size(500, 500)

def draw():
    background(1, 1, 1)
    m.display()

def update(dt):
    m.update()

if __name__ == "__main__":
    run()