import turtle as tt
import modules.tank as tank


def first_player_fire():

    ball = tt.Turtle("circle")
    ball.speed(0)
    ball.color("black")
    ballSize = 0.3
    ball.shapesize(ballSize, ballSize)
    ball.penup()
    ball.goto(tank.get_tank_position(tank.first_player))
    ball._tracer(0)
    # while ball.xcor() <= 720 and ball.ycor() <= 580:
    #    ball.forward(1)


def second_player_fire():

    ball = tt.Turtle("circle")
    ball.speed(0)
    ball.color("black")
    ballSize = 0.3
    ball.shapesize(ballSize, ballSize)
    ball.penup()
    ball.goto(tank.get_tank_position(tank.second_player))
    ball._tracer(0)
    # while ball.xcor() <= 720 and ball.ycor() <= 580:
    #    ball.forward(1)
