import turtle as tt
import modules.tank as tank
from math import atan2, degrees, cos, sin, pi

first_player_ball = None
second_player_ball = None
navigation_map = []


def create_ball(player):
    ball = tt.Turtle("circle")
    ball.hideturtle()
    ball.speed(0)
    ball.color("black")
    ball_size = 0.3
    ball.shapesize(ball_size, ball_size)
    ball.penup()
    ball.goto(tank.get_tank_position(player))
    ball._tracer(0)
    return ball


def first_player_fire():
    ball = first_player_ball
    if not tank.is_some_tank_respawning() and ball.isvisible() is False:
        ball.goto(tank.get_tank_position(tank.first_player))
        ball._tracer(0)
        ball.setheading(0)
        ball.right(tank.get_tank_angle(tank.first_player))
        ball.forward(35)
        ball.showturtle()


def second_player_fire():
    ball = second_player_ball
    if not tank.is_some_tank_respawning() and ball.isvisible() is False:
        ball.goto(tank.get_tank_position(tank.second_player))
        ball._tracer(0)
        ball.setheading(0)
        ball.right(tank.get_tank_angle(tank.second_player))
        ball.forward(35)
        ball.showturtle()


def move_ball(ball, player, target):
    if ball.isvisible() is True:
        # Atribuindo ângulo do tanque à bola
        ball.setheading(0)
        ball.right(tank.get_tank_angle(player))

        # Verificando se colisão bola-mapa
        ball_x, ball_y = [10 * sin(ball.heading()*pi/180)+ball.xcor(),
                          10 * cos(ball.heading()*pi/180)+ball.ycor()]
        ball_x, ball_y = int((ball_x+360)/20), int((ball_y+290)/20)
        if not navigation_map[28-ball_y][ball_x]:
            ball.forward(15)
        else:
            ball.hideturtle()

        # Verificando se colisão bola-tanque
        x, y = tank.get_tank_position(target)
        if (x-20 <= ball.xcor() <= x + 20 and y-20 <= ball.ycor() <= y + 20):
            ball.hideturtle()
            target.is_respawning = True
        if ball.xcor() >= 360 or ball.xcor() <= -360 or ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.hideturtle()
