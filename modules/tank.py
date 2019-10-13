import turtle as tt
from math import atan2, degrees, cos, sin, pi

first_player = None
second_player = None


def register_tank_shape(screen):
    points = ((-3, 10), (-3, 30), (3, 30), (3, 10),
              (10, 10), (10, 15), (20, 15), (20, -15),
              (10, -15), (10, -5), (-10, -5), (-10, -15),
              (-20, -15), (-20, 15), (-10, 15), (-10, 10))
    screen.register_shape("tank", points)


def create_player(color, x, y):
    tank = ()
    tank = tt.Turtle()
    tank.shape("tank")
    tank.color(color)
    tank.penup()
    tank.dx = 0
    tank.dy = 0
    tank.goto(x, y)
    return tank


def first_player_walk():
    print("a")


def first_player_rotate_left():
    player = first_player
    player.left(30)


def first_player_rotate_right():
    player = first_player
    player.left(30)


def second_player_walk():
    print("d")


def second_player_rotate_left():
    player = second_player
    player.left(30)


def second_player_rotate_right():
    player = second_player
    player.right(30)


def get_tank_angle(tank):
    return tank.heading()


def get_tank_position(tank):
    return (tank.xcor(), tank.ycor())
