import turtle as tt


def ball():

    # criando uma tela para testes
    testScreen = tt.Screen()
    testScreen.title("Test")
    testScreen.bgcolor("lightgreen")
    testScreen.setup(1366, 768)
    testScreen.update

    turn = 45

    # simulando um tanque
    tank = tt.Turtle("square")
    tank.speed(0)
    tank.color("blue")
    tank.shapesize(3, 3)
    tank.goto(500, 100)
    tank.left(turn)
    tank.penup

    cannon = tt.Turtle("square")
    cannon.speed(0)
    cannon.color("red")
    cannon.shapesize(0.5, 0.5)
    cannon.goto(tank.xcor()-30, tank.ycor())
    cannon.left(turn)
    cannon.penup

    ball = tt.Turtle("circle")
    ball.speed(10)
    ball.color("black")
    ballSize = 0.3
    ball.shapesize(ballSize, ballSize)
    ball.goto(cannon.xcor(), cannon.ycor())
    ball.penup

    # def fire():


ball()
