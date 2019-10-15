import turtle as tt

def generate(level):
    # manipulação do arquivo
    #file = open('/home/williams_gomes/vscode/github/atari-combat-tank/level1.txt')
    file = open(level)
    lvl = file.readlines()
    for i in range(len(lvl)):
        lvl[i] = lvl[i].strip('\n')
    
    # x e y baseado nas dimensões da tela
    x = -350
    y = 280

    for i in range(29):
        for j in range(36):
            if lvl[i][j] != '0':
                    block = tt.Turtle()
                    block.shape("square")
                    block.color("white")
                    block.shapesize(1, 1)
                    block.penup()
                    block.goto(x, y)
            x += 20
        y -= 20
        x = -350
        
    file.close()