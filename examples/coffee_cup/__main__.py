from yap5 import *
from coffeecup import CoffeCup
from pyglet.window import key

w = 1000
h = 1000

cup = CoffeCup(Vector(w/2, h/2), radius=h/2 - 100, num_of_points=100, times_table=2)


def setup():
    size(w, h)
    window.on_key_press = key_press


def draw():
    background(Color("white"))
    cup.draw()


def key_press(symbol, modifiers):
    if symbol == key.UP:
        cup.table += 1
        cup.calc_points()
    elif symbol == key.DOWN:
        cup.table -= 1
        cup.calc_points()
    elif symbol == key.RIGHT:
        cup.n_points += 10
    elif symbol == key.LEFT:
        cup.n_points -= 10
    elif symbol == key.SPACE:
        print("Times Table:", cup.table)
        print("N points:", cup.n_points)
        print()


run()
