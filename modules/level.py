import turtle as tt

def generate(file):
    # manipulação do arquivo
    #file = open('/home/williams_gomes/vscode/github/atari-combat-tank/level1.txt')
    level = open(file)
    lvl = level.readlines()
    for i in range(len(lvl)):
        lvl[i] = lvl[i].strip('\n')
    
    # x e y baseado nas dimensões da tela
    x = -350
    y = 280

    for i in range(29):
        for j in range(36):
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


def nav_generate(file):
    # manipulação do arquivo
    level = open(file)
    nav = level.readlines()
    for i in range(len(nav)):
        nav[i] = nav[i].strip('\n')

    # x e y baseado nas dimensões da tela
    x = -350
    y = 280
    navigation_mesh = []

    for i in range(58):
        navigation_mesh.append([0] * 72)
        for j in range(72):
            navigation_mesh[i][j] = int(nav[i][j])
            x += 10
        y -= 10
        x = -350
    return navigation_mesh