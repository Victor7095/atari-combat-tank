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

    screen.mainloop()
