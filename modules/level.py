import turtle as tt


def create_block(x, y):
    block = tt.Turtle()
    block.shape("square")
    block.color("white")
    block.shapesize(1, 1)
    block.penup()
    block.goto(x, y)


def generate():
    # manipulação do arquivo

    # file = open('level1.txt')
    file = open(
        '/home/williams_gomes/vscode/github/atari-combat-tank/level1.txt')

    lab = file.readlines()
    for i in range(len(lab)):
        lab[i] = lab[i].strip('\n')

    # matriz constante que possui todas as coordenadas dos blocos (vazios ou nao)
    # (29 linhas, 36 colunas)
    MATRIX = []
    # lista que possui coordenadas dos blocos desenhados
    gamelevel = []

    i = 0
    j = 0
    x = -350
    y = 280
    while i < 29:
        MATRIX.append([0] * 36)
        while j < 36:
            MATRIX[i][j] = [x, y]
            if lab[i][j] != '0':
                create_block(x, y)  # função gera blocos
                gamelevel.append([x, y])
            x += 20
            j += 1
        y -= 20
        x = -350
        i += 1
        j = 0
