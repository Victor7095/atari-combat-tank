import turtle as tt
import modules.tank as tank

first_player_ball = None
second_player_ball = None


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
        return ball


def second_player_fire():
    ball = second_player_ball
    if not tank.is_some_tank_respawning() and ball.isvisible() is False:
        ball.goto(tank.get_tank_position(tank.second_player))
        ball._tracer(0)
        ball.setheading(0)
        ball.right(tank.get_tank_angle(tank.second_player))
        ball.forward(35)
        ball.showturtle()
        return ball


def move_ball(ball, player, target):
    if ball.isvisible() is True:
        ball.setheading(0)
        ball.right(tank.get_tank_angle(player))
        ball.forward(10)
    x, y = tank.get_tank_position(target)
    if (x-20 <= ball.xcor() <= x + 20 and y-20 <= ball.ycor() <= y + 20):
        ball.hideturtle()
        target.is_respawning = True
    if ball.xcor() >= 360 or ball.xcor() <= -360 or ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.hideturtle()
    return ball
