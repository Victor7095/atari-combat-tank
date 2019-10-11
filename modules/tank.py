import turtle as tt
from math import atan2, degrees, cos, sin, pi

first_player = {}
second_player = {}


def create_player(color, x, y):
    tank = {}
    tank["parts"] = []
    tank["dx"] = 0
    tank["dy"] = 0

    for _ in range(4):
        tank_part = tt.Turtle()
        tank_part.shape("square")
        tank_part.color(color)
        tank_part.penup()
        tank["parts"].append(tank_part)

    tank["parts"][0].goto(x, y)
    tank["parts"][0].turtlesize(0.75, 1)
    tank["parts"][1].goto(x+15, y-3)
    tank["parts"][1].turtlesize(1.5, 0.5)
    tank["parts"][2].goto(x-15, y-3)
    tank["parts"][2].turtlesize(1.5, 0.5)
    tank["parts"][3].goto(x, y+15)
    tank["parts"][3].turtlesize(1, 0.25)
    return tank


def first_player_walk():
    print("a")


def first_player_rotate_left():
    print("b")


def first_player_rotate_right():
    print("c")


def second_player_walk():
    print("d")


def second_player_rotate_left():
    print("e")


def second_player_rotate_right():
    print("f")
