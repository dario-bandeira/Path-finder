class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    grey = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INV = '\033[0m'
    black = '\033[30m'


largura = 50
altura = 50

matrix = [[" " for y in range(altura)] for x in range(largura)]


def print_matrix():
    for x in matrix:
        for y in x:
            if len(str(y)) == 1:
                print("0", end="")
            print(y, end='')
            # print("%02d" % y, end="")
        print("")


def expande(x, y):
    global matrix
    if type(matrix[x][y]) == int:
        numero_atual = matrix[x][y]
        # esquerda
        if y > 0 and matrix[x][y-1] == " ":
            matrix[x][y-1] = numero_atual + 1
        # cima
        if x > 0 and matrix[x-1][y] == " ":
            matrix[x-1][y] = numero_atual + 1
        # direita
        if y <= largura - 2 and matrix[x][y+1] == " ":
            matrix[x][y+1] = numero_atual + 1
        # baixo
        if x <= altura - 2 and matrix[x+1][y] == " ":
            matrix[x+1][y] = numero_atual + 1


def cheio():
    for i, x in enumerate(matrix):
        if " " in x:
            print(i)
            return
    print("cheio")


matrix[25][25] = 0
maior = 0

for z in range(50):
    for x in range(altura):
        for y in range(largura):
            if matrix[x][y] == maior:
                expande(x, y)

    for x in range(altura - 1, -1, -1):
        for y in range(largura - 1, -1, -1):
            if matrix[x][y] == maior:
                expande(x, y)

    maior += 1

cheio()

print_matrix()
