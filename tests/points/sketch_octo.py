import sys
sys.path.append('D:/code/octo')
from octo import *

def setup():
    size(600, 600)

def draw():
    background(Color('white'))
    point(Vector(300, 300))

if __name__ == "__main__":
    run()
