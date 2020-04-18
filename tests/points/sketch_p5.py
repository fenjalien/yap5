from p5 import *

p: PShape# = PShape([(300, 300, 0)], attribs='point')

def setup():
    size(600, 600)
    global p
    p = PShape([(300, 300, 0)], attribs='point')

def draw():
    background(255)
    point(300, 300)
    

if __name__ == "__main__":
    run()