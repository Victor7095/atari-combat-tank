import turtle as tt
import modules.tank as tank


def ball(player):

    ball = tt.Turtle("circle")
    ball.speed(10)
    ball.color("black")
    ballSize = 0.3
    ball.shapesize(ballSize, ballSize)
    ball.goto(tank.get_tank_position(player))
    ball.penup

    # def fire():
