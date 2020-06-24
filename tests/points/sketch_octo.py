import sys
sys.path.append('D:/code/octo')
from yap5 import *
from random import randint

# vs = [Vector(randint(100, 500), randint(100, 500)) for i in range(10)]

def setup():
    size(600, 600)

def draw():
    background(Color('white'))
    # lines([Vector(200, 100), Vector(300, 500), Vector(300, 400), Vector(500, 100)])
    triangle(Vector(200, 200), Vector(300, 300), Vector(400, 300), theme=Theme(fill=Color('red'), stroke_weight=5))

if __name__ == "__main__":
    run() 