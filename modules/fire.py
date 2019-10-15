import turtle as tt
import modules.tank as tank

first_player_ball = None
second_player_ball = None


def create_ball(player):
    ball = tt.Turtle("circle")
    ball.hideturtle()
    ball.speed(0)
    ball.color("black")
    ballSize = 0.3
    ball.shapesize(ballSize, ballSize)
    ball.penup()
    ball.goto(tank.get_tank_position(player))
    ball._tracer(0)
    return ball


def first_player_fire():
    ball = first_player_ball
    if ball.isvisible() is False:
        ball.goto(tank.get_tank_position(tank.first_player))
        ball._tracer(0)
        ball.setheading(0)
        ball.right(tank.get_tank_angle(tank.first_player))
        ball.forward(35)
        ball.showturtle()
    return ball


def second_player_fire():
    ball = second_player_ball
    if ball.isvisible() is False:
        ball.goto(tank.get_tank_position(tank.second_player))
        ball._tracer(0)
        ball.setheading(0)
        ball.right(tank.get_tank_angle(tank.second_player))
        ball.forward(35)
        ball.showturtle()
    return ball


def move_ball(player):
    ball = player
    if ball.isvisible() is True:
        ball.forward(30)

    if ball.xcor() >= 360 or ball.xcor() <= -360 or ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.hideturtle()
    return ball
