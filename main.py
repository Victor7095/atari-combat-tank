import turtle as tt
import modules.tank as tank
import modules.level as level
import modules.fire as fire
screen = None

screen = tt.Screen()
print(screen.screensize())
screen.clear()
screen.title("Atari Combat Tank")
screen.bgcolor("yellowgreen")
screen.setup(720, 580)  # 720,480 antigo
screen.tracer(0)
screen.mode("logo")

command_history = set()

tank.register_tank_shape(screen)

tank.first_player = tank.create_player("red", -190, 0)
tank.second_player = tank.create_player("blue", 190, 0)

# a função agora pede o nivel que se deseja criar como argumento
level.generate('level1.txt')


def w():
    command_history.add(tank.first_player_walk)


def stop_w():
    command_history.discard(tank.first_player_walk)


def u():
    command_history.add(tank.second_player_walk)


def stop_u():
    command_history.discard(tank.second_player_walk)


screen.listen()
screen.onkeypress(w, "w")
screen.onkeyrelease(stop_w, "w")
screen.onkeypress(tank.first_player_rotate_left, "a")
screen.onkeypress(tank.first_player_rotate_right, "d")
screen.onkeypress(u, "Up")
screen.onkeyrelease(stop_u, "Up")
screen.onkeypress(fire.first_player_fire, "s")

screen.onkeypress(tank.second_player_rotate_left, "Left")
screen.onkeypress(tank.second_player_rotate_right, "Right")
screen.onkeypress(fire.second_player_fire, "Down")


def run():
    screen.update()
    for b in command_history:
        b()
    screen.ontimer(run, 30)


screen.ontimer(run, 1)
screen.mainloop()
