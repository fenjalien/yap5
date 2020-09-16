from yap5 import *
from src import CoffeCup
from pyglet.window import key

cup = CoffeCup(Vector(500, 500), radius=400, num_of_points=100, times_table=21)


def setup():
    size(1000, 1000)
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
    print(cup.table)


run()
