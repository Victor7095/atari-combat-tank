import turtle as tt
import modules.tank as tank
import modules.level as level
import modules.fire as fire

screen = tt.Screen()
screen.clear()
screen.title("Atari Combat Tank")
screen.bgcolor("yellowgreen")
screen.setup(720, 580)  # 720,480 antigo
print(screen.screensize())
screen.tracer(0)
screen.mode("logo")

command_history = set()

tank.register_tank_shape(screen)

tank.first_player = tank.create_player("red", -190, 0)
fire.first_player_ball = fire.create_ball(tank.first_player)
tank.second_player = tank.create_player("blue", 190, 0)
fire.second_player_ball = fire.create_ball(tank.second_player)

# a função agora pede o nivel que se deseja criar como argumento
tank.navigation_map = level.generate('level1.txt')


# Comandos primeiro jogador
def start_first_player_walk():
    command_history.add(tank.first_player_walk)


def stop_first_player_walk():
    command_history.discard(tank.first_player_walk)


def start_first_player_rotate_left():
    command_history.add(tank.first_player_rotate_left)


def stop_first_player_rotate_left():
    command_history.discard(tank.first_player_rotate_left)


def start_first_player_rotate_right():
    command_history.add(tank.first_player_rotate_right)


def stop_first_player_rotate_right():
    command_history.discard(tank.first_player_rotate_right)


# Comandos segundo jogador
def start_second_player_walk():
    command_history.add(tank.second_player_walk)


def stop_second_player_walk():
    command_history.discard(tank.second_player_walk)


def start_second_player_rotate_left():
    command_history.add(tank.second_player_rotate_left)


def stop_second_player_rotate_left():
    command_history.discard(tank.second_player_rotate_left)


def start_second_player_rotate_right():
    command_history.add(tank.second_player_rotate_right)


def stop_second_player_rotate_right():
    command_history.discard(tank.second_player_rotate_right)


screen.listen()
screen.onkeypress(start_first_player_walk, "w")
screen.onkeyrelease(stop_first_player_walk, "w")
screen.onkeypress(start_first_player_rotate_left, "a")
screen.onkeyrelease(stop_first_player_rotate_left, "a")
screen.onkeypress(start_first_player_rotate_right, "d")
screen.onkeyrelease(stop_first_player_rotate_right, "d")
screen.onkeypress(fire.first_player_fire, "s")

screen.onkeypress(start_second_player_walk, "Up")
screen.onkeyrelease(stop_second_player_walk, "Up")
screen.onkeypress(start_second_player_rotate_left, "Left")
screen.onkeyrelease(stop_second_player_rotate_left, "Left")
screen.onkeypress(start_second_player_rotate_right, "Right")
screen.onkeyrelease(stop_second_player_rotate_right, "Right")
screen.onkeypress(fire.second_player_fire, "Down")


def run():
    screen.update()
    fire.move_ball(fire.first_player_ball, tank.first_player)
    fire.move_ball(fire.second_player_ball, tank.second_player)
    for command in command_history:
        command()
    screen.ontimer(run, 1)


screen.ontimer(run, 1)
screen.mainloop()
