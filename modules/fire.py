import turtle as tt
import modules.tank as tank


def ball(player):

    ball = tt.Turtle("circle")
    ball.speed(0)
    ball.color("black")
    ballSize = 0.3
    ball.shapesize(ballSize, ballSize)
    ball.penup()
    ball.goto(tank.get_tank_position(player))
    ball._tracer(0)
    # while ball.xcor() <= 720 and ball.ycor() <= 580:
    #    ball.forward(1)
