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
    if color == 'red':
        tank.right(90)
    else:
        tank.left(90)
    tank.goto(x, y)
    tank.is_respawning = False
    tank.respawn_time = 100
    tank.score = 0
    return tank


def first_player_walk():
    player = first_player
    set_tank_position_in_matrix(player)
    if (navigation_map[28-player.y][player.x] or
            navigation_map[28-player.y2][player.x2] or
            navigation_map[28-player.y3][player.x3]):
        player.backward(5)
    else:
        player.forward(2)


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
    alpha = tank.heading()
    x, y = [25 * sin(alpha*pi/180)+tank.xcor(),
            25 * cos(alpha*pi/180)+tank.ycor()]
    x2, y2 = [15 * sin((alpha+45)*pi/180)+tank.xcor(),
              15 * cos((alpha+45)*pi/180)+tank.ycor()]
    x3, y3 = [15 * sin((alpha-45)*pi/180)+tank.xcor(),
              15 * cos((alpha-45)*pi/180)+tank.ycor()]
    # print("{} {} ({:.2f},{:.2f}) ({:.2f},{:.2f})".format(
    #    tank.heading(), tank.heading()*pi/180, tank.xcor(), tank.ycor(), x, y))
    tank.x, tank.y = int((x+360)/20), int((y+290)/20)
    tank.x2, tank.y2 = int((x2+360)/20), int((y2+290)/20)
    tank.x3, tank.y3 = int((x3+360)/20), int((y3+290)/20)


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
    adjacent_positions = [navigation_map[i][j]
                          for [i, j] in adjacent_positions]
    while any(adjacent_positions):
        i, j = randint(6, 27), randint(1, 34)
        adjacent_positions = [[i - 1, j - 1],
                              [i, j - 1],
                              [i + 1, j - 1],
                              [i - 1, j + 1],
                              [i, j + 1],
                              [i + 1, j + 1],
                              [i - 1, j],
                              [i + 1, j]]
        adjacent_positions = [navigation_map[i][j]
                              for [i, j] in adjacent_positions]
    return ((28-i)*20)-280, (j*20)-350


def die(tank):
    tank.respawn_time -= 1
    if tank.respawn_time > 0:
        tank.left(15)
    else:
        i, j = create_random_position()
        tank.goto(j, i)
        tank.is_respawning = False
        tank.respawn_time = 100
        if tank == first_player:
            second_player.score += 1
        if tank == second_player:
            first_player.score += 1


def is_some_tank_respawning():
    return first_player.is_respawning or second_player.is_respawning
