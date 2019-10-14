# função create_menu chamada na main.py
# receber como parâmetro o screen (declarado na main) e uma variável que \
# armazena a opção selecionada
# com o screen, adicionar eventos para a opção do menu e quando selecionada,\
# muda o valor da segunda variável que armazena a resposta
# no loop principal, a variável deve receber um valor válido
import turtle as tt


def create_menu(screen, option):
    pass

if __name__ == "__main__":
    print("oi")
    screen = tt.Screen()
    print(screen.screensize())
    screen.clear()
    screen.title("Atari Combat Tank")
    screen.bgcolor("black")
    screen.setup(720, 580)  # 720,480 antigo
    screen.tracer(0)
    screen.mode("logo")
    screen.mainloop()