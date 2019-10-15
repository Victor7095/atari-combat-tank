# função create_menu chamada na main.py
# receber como parâmetro o screen (declarado na main) e uma variável que \
# armazena a opção selecionada
# com o screen, adicionar eventos para a opção do menu e quando selecionada,\
# muda o valor da segunda variável que armazena a resposta
# no loop principal, a variável deve receber um valor válido
import turtle as tt


def create_menu(screen, option):
    pass


# criando tela de menu
if __name__ == "__main__":
    screen = tt.Screen()
    screen.clear()
    screen.title("Atari Combat Tank")
    screen.bgcolor("black")
    screen.setup(720, 580)
    screen.tracer(0)
    screen.mode("logo")

    # desenhando o título
    import turtle
    title = turtle
    title.setposition(0, 225)
    title.color("yellow")
    style = ("Fixedsys", 30, "bold")
    title.write("ATARI COMBAT TANK", font=style, align="center")
    title.hideturtle()

    # desenhando opções

    play = turtle
    play.setposition(0, 50)
    play.color("yellow")
    style = ("Fixedsys", 20, "bold")
    play.write("play game", font=style, align="center")
    play.hideturtle()

    credit = turtle
    credit_position_x = 0
    credit_position_y = 0
    credit.setposition(credit_position_x, credit_position_y)
    credit.color("yellow")
    style = ("Fixedsys", 20, "bold")
    credit.write("credits", font=style, align="center")
    credit.hideturtle()

    exit_game = turtle
    exit_position_x = 0
    exit_position_y = -50
    exit_game.setposition(exit_position_x, exit_position_y)
    exit_game.color("yellow")
    style = ("Fixedsys", 20, "bold")
    exit_game.write("exit", font=style, align="center")
    exit_game.hideturtle()

    # lógica do exit

    def end_game(a, b):
        if(exit_position_x - 40 <= a <= exit_position_x + 40 and
           exit_position_y - 40 <= b <= exit_position_y + 40):
            screen.bye()

    # lógica do credits

    def credits_(a, b):
        if(credit_position_x - 40 <= a <= credit_position_x + 40 and
           credit_position_y - 40 <= b <= credit_position_y + 40):
            credit.clear()
            developers = turtle
            developers_position_x = 0
            developers_position_y = 70
            credit.setposition(developers_position_x, developers_position_y)
            credit.color("yellow")
            style = ("Fixedsys", 30, "bold")
            credit.write(
                "DEVELOPERS\n\n\n", font=style, align="center")
            credit.hideturtle()
            names = turtle
            names_position_x = 0
            names_position_y = -170
            credit.setposition(names_position_x, names_position_y)
            credit.color("yellow")
            style = ("Fixedsys", 25, "bold")
            credit.write(
                "Gabriel\n\nVanessa\n\nVictor\n\nVinicius\n\nWilliams",
                font=style, align="center")
            credit.hideturtle()

    def call(a, b):
        credits_(a, b)
        end_game(a, b)
    screen.onscreenclick(call)

    screen.mainloop()
