import turtle as tt
from math import atan2, degrees, cos, sin, pi

first_player = {}
second_player = {}

ROTATE_LEFT = 1
ROTATE_RIGHT = 2


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
    parts = first_player["parts"]
    rotate(parts, ROTATE_LEFT)


def first_player_rotate_right():
    parts = first_player["parts"]
    rotate(parts, ROTATE_RIGHT)


def second_player_walk():
    print("d")


def second_player_rotate_left():
    parts = second_player["parts"]
    rotate(parts, ROTATE_LEFT)


def second_player_rotate_right():
    parts = second_player["parts"]
    rotate(parts, ROTATE_RIGHT)


def rotate(parts, direction):
    # Coordenadas do centro
    [x1, y1] = [parts[0].xcor(), parts[0].ycor()]

    # Novos ângulos das outras partes
    for i in range(1, 4):
        [x2, y2] = [parts[i].xcor(), parts[i].ycor()]
        [new_x, new_y] = new_part_position(x1, y1, x2, y2, direction)
        parts[i].goto(new_x, new_y)

    if direction == ROTATE_LEFT:
        for i in range(len(parts)):
            parts[i].left(10)
    elif direction == ROTATE_RIGHT:
        for i in range(len(parts)):
            parts[i].right(10)


def new_part_position(x1, y1, x2, y2, direction):
    # Distância do centro da parte central até o centro de outra parte
    r = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

    # Delta X & Delta Y
    [dx, dy] = [x2-x1, y2-y1]

    # Ângulo em radinaos
    rad = atan2(dy, dx)

    # Subtrai/Soma 10 graus dependendo do sentido da rotação
    if direction == ROTATE_LEFT:
        rad += 0.174533
    elif direction == ROTATE_RIGHT:
        rad -= 0.174533

    # Nova posição da parte do tanque
    x = x1 + r * cos(rad)
    y = y1 + r * sin(rad)

    return (x, y)
