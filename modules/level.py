import turtle as tt


def generate(file):
    # manipulação do arquivo
    #file = ('/home/williams_gomes/vscode/github/atari-combat-tank/level1.txt')
    level = open(file)
    lvl = level.readlines()
    for i in range(len(lvl)):
        lvl[i] = lvl[i].strip('\n')

    # x e y baseado nas dimensões da tela
    x = -350
    y = 280

    navigation_mesh = []

    for i in range(29):
        navigation_mesh.append([0] * 36)
        for j in range(36):
            navigation_mesh[i][j] = int(lvl[i][j])
            if int(lvl[i][j]):
                block = tt.Turtle()
                block.shape("square")
                block.color("white")
                block.shapesize(1, 1)
                block.penup()
                block.goto(x, y)
            x += 20
        y -= 20
        x = -350

    level.close()
    return navigation_mesh
