import turtle as tt
import modules.tank as tank
import modules.level as level
import modules.fire as fire
import modules.menu as menu
from sys import argv
from time import sleep

screen = tt.Screen()
map_name = argv[1]
command_history = set()
hud1 = None
hud2 = None


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
    hud1.write("0", align="center", font=("Press Start 2P", 48, "normal"))

    hud2 = tt.Turtle()
    hud2.speed(0)
    hud2.shape("square")
    hud2.color("blue")
    hud2.penup()
    hud2.hideturtle()
    hud2.goto(250, 200)
    hud2.write("0", align="center", font=("Press Start 2P", 48, "normal"))

    tank.register_tank_shape(screen)
    tank.first_player = tank.create_player("red", -280, -50)
    fire.first_player_ball = fire.create_ball(tank.first_player)
    tank.second_player = tank.create_player("blue", 280, -50)
    fire.second_player_ball = fire.create_ball(tank.second_player)

    tank.navigation_map = fire.navigation_map = level.generate(map_name)

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


def game_over(player, color):
    game_over_lbl = tt.Turtle()
    game_over_lbl.speed(0)
    game_over_lbl.shape("square")
    game_over_lbl.color(color)
    game_over_lbl.penup()
    game_over_lbl.hideturtle()
    game_over_lbl.goto(0, 0)
    game_over_lbl.write("{} WIN!".format(player), align="center", font=(
        "Press Start 2P", 48, "normal"))
    sleep(5)


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

    # Renderização do menu
    if len(menu.jogar) > 0 and menu.jogar[0] == "creating_menu":
        menu.create_menu(screen)
        menu.jogar[0] = "waiting"

    # Renderização do mapa
    if len(menu.jogar) > 0 and menu.jogar[0] == "starting":
        hud1, hud2 = create_game()
        menu.jogar[0] = "playing"

    # Jogo em execução
    if len(menu.jogar) > 0 and menu.jogar[0] == "playing":
        # Movimentação das balas
        fire.move_ball(fire.first_player_ball,
                       tank.first_player, tank.second_player)
        fire.move_ball(fire.second_player_ball,
                       tank.second_player, tank.first_player)

        # Renascimento do primeiro jogador
        if tank.first_player.is_respawning:
            tank.die(tank.first_player)
        hud2.clear()
        hud2.write("{}".format(tank.second_player.score),
                   align="center", font=("Press Start 2P", 48, "normal"))

        # Renascimento do segundo jogador
        if tank.second_player.is_respawning:
            tank.die(tank.second_player)
        hud1.clear()
        hud1.write("{}".format(tank.first_player.score),
                   align="center", font=("Press Start 2P", 48, "normal"))

        # Game Over
        if tank.first_player.score == 1 or tank.second_player.score == 1:
            if tank.first_player.score == 1:
                winner = "Player 1"
                color = "red"
            if tank.second_player.score == 1:
                winner = "Player 2"
                color = "blue"
            game_over(winner, color)
            menu.jogar[0] = "creating_menu"

        # Executando movimentos pressionados
        for command in command_history:
            command()

    screen.update()
    screen.ontimer(run, 1)


screen.ontimer(run, 1)
screen.mainloop()
