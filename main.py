import turtle as tt
import modules.tank as tank
import modules.level as level

screen = None

screen = tt.Screen()
print(screen.screensize())
screen.clear()
screen.title("Little Breakout ")
screen.bgcolor("yellowgreen")
screen.setup(720, 580)  # 720,480 antigo
screen.tracer(0)

tank.first_player = tank.create_player("red", -200, 0)
tank.second_player = tank.create_player("blue", 200, 0)

level.generate()

screen.listen()
screen.onkeypress(tank.first_player_walk, "w")
screen.onkeypress(tank.first_player_rotate_left, "a")
screen.onkeypress(tank.first_player_rotate_right, "d")
screen.onkeypress(tank.second_player_walk, "Up")
screen.onkeypress(tank.second_player_rotate_left, "Left")
screen.onkeypress(tank.second_player_rotate_right, "Right")


def run():
    screen.update()
    screen.ontimer(run, 1)


screen.ontimer(run, 1)
screen.mainloop()
