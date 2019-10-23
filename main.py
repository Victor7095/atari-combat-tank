import turtle as tt
import modules.tank as tank
import modules.level as level
import modules.fire as fire
import modules.menu as menu

screen = tt.Screen()
command_history = set()
hud1 = None
hud2 = None
score_1 = 0
score_2 = 0


def create_game():
    command_history.clear()
    print(screen.screensize())
    screen.clear()
    screen.title("Atari Combat Tank")
    screen.bgcolor("#88AA00")
    screen.setup(720, 580)  # 720,480 antigo
    screen.tracer(0)
    screen.mode("logo")

    hud1 = tt.Turtle()
    hud1.speed(0)
    hud1.shape("square")
    hud1.color("red")
    hud1.penup()
    hud1.hideturtle()
    hud1.goto(-250, 200)
    hud1.write("0", align="center", font=("Press Start 2P",48,"normal") )

    hud2 = tt.Turtle()
    hud2.speed(0)
    hud2.shape("square")
    hud2.color("blue")
    hud2.penup()
    hud2.hideturtle()
    hud2.goto(250, 200)
    hud2.write("0", align="center", font=("Press Start 2P",48,"normal") )

    tank.register_tank_shape(screen)
    tank.first_player = tank.create_player("red", -280, -50)
    fire.first_player_ball = fire.create_ball(tank.first_player)
    tank.second_player = tank.create_player("blue", 280, -50)
    fire.second_player_ball = fire.create_ball(tank.second_player)
    tank.navigation_map = level.generate("level1.txt")

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

    return hud1, hud2


# Comandos primeiro jogador
def start_first_player_walk():
    if not tank.is_some_tank_respawning():
        command_history.add(tank.first_player_walk)


def stop_first_player_walk():
    command_history.discard(tank.first_player_walk)


def start_first_player_rotate_left():
    if not tank.is_some_tank_respawning():
        command_history.add(tank.first_player_rotate_left)


def stop_first_player_rotate_left():
    command_history.discard(tank.first_player_rotate_left)


def start_first_player_rotate_right():
    if not tank.is_some_tank_respawning():
        command_history.add(tank.first_player_rotate_right)


def stop_first_player_rotate_right():
    command_history.discard(tank.first_player_rotate_right)


# Comandos segundo jogador
def start_second_player_walk():
    if not tank.is_some_tank_respawning():
        command_history.add(tank.second_player_walk)


def stop_second_player_walk():
    command_history.discard(tank.second_player_walk)


def start_second_player_rotate_left():
    if not tank.is_some_tank_respawning():
        command_history.add(tank.second_player_rotate_left)


def stop_second_player_rotate_left():
    command_history.discard(tank.second_player_rotate_left)


def start_second_player_rotate_right():
    if not tank.is_some_tank_respawning():
        command_history.add(tank.second_player_rotate_right)


def stop_second_player_rotate_right():
    command_history.discard(tank.second_player_rotate_right)


def run():
    global hud1
    global hud2
    global score_1
    global score_2
    if len(menu.jogar) > 0 and menu.jogar[0] == "creating_menu":
        menu.create_menu(screen)
        menu.jogar[0] = "waiting"
    if len(menu.jogar) > 0 and menu.jogar[0] == "starting":
        hud1, hud2 = create_game()
        menu.jogar[0] = "playing"
    if len(menu.jogar) > 0 and menu.jogar[0] == "playing":
        fire.move_ball(fire.first_player_ball,
                       tank.first_player, tank.second_player)
        fire.move_ball(fire.second_player_ball,
                       tank.second_player, tank.first_player)
        if tank.first_player.is_respawning:
            tank.die(tank.first_player)
            score_2 += 1
            hud2.clear()
            hud2.write("{}".format(score_2), align="center", font=("Press Start 2P",48,"normal") )
        if tank.second_player.is_respawning:
            tank.die(tank.second_player)
            score_1 += 1
            hud1.clear()
            hud1.write("{}".format(score_1), align="center", font=("Press Start 2P",48,"normal") )
        for command in command_history:
            command()
    screen.update()
    screen.ontimer(run, 1)


screen.ontimer(run, 1)
screen.mainloop()
