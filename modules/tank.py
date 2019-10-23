import turtle as tt
from math import atan2, degrees, cos, sin, pi
from random import randint

first_player = None
second_player = None
navigation_map = []


def register_tank_shape(screen):
    """points = ((-1.5, 2), (-1.5, 10), (1.5, 10), (1.5, 2),
              (5, 2), (5, 6), (10, 6), (10, -10),
              (5, -10), (5, -3), (-5, -3), (-5, -10),
              (-10, -10), (-10, 6), (-5, 6), (-5, 2))"""
    points = ((-3, 10), (-3, 25), (3, 25), (3, 10),
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
    player = first_player
    set_tank_position_in_matrix(player)
    if not navigation_map[28-player.y][player.x]:
        player.forward(2)
    else:
        player.backward(10)


def first_player_rotate_left():
    player = first_player
    player.left(10)


def first_player_rotate_right():
    player = first_player
    player.right(10)


def second_player_walk():
    player = second_player
    set_tank_position_in_matrix(player)
    if not navigation_map[28-player.y][player.x]:
        player.forward(2)
    else:
        player.backward(10)


def second_player_rotate_left():
    player = second_player
    player.left(10)


def second_player_rotate_right():
    player = second_player
    player.right(10)


def get_tank_angle(tank):
    return tank.heading()


def get_tank_position(tank):
    return (tank.xcor(), tank.ycor())


def set_tank_position_in_matrix(tank):
    x, y = [20 * sin(tank.heading()*pi/180)+tank.xcor(),
            20 * cos(tank.heading()*pi/180)+tank.ycor()]
    # print("{} {} ({:.2f},{:.2f}) ({:.2f},{:.2f})".format(
    #    tank.heading(), tank.heading()*pi/180, tank.xcor(), tank.ycor(), x, y))
    tank.x, tank.y = int((x+360)/20), int((y+290)/20)


def create_random_position():
    i, j = randint(6, 27), randint(1, 34)
    adjacent_positions = [[i - 1, j - 1],
                          [i, j - 1],
                          [i + 1, j - 1],
                          [i - 1, j + 1],
                          [i, j + 1],
                          [i + 1, j + 1],
                          [i - 1, j],
                          [i + 1, j]]
    print(adjacent_positions)
    adjacent_positions = [navigation_map[i][j]
                          for [i, j] in adjacent_positions]
    while any(adjacent_positions):
        i, j = randint(6, 27), randint(1, 34)
        adjacent_positions = navigation_map[i-1:i+2][j-1: j+2]
    return i*20-280, j*20-360


def die(screen, tank, ms):
    tank.ms = ms

    def spin():
        tank.left(6)
        tank.ms -= 1
        print(tank.ms)
        if tank.ms > 0:
            screen.ontimer(spin, 1)
        else:
            tank.goto(create_random_position())
    screen.ontimer(spin, 1)
