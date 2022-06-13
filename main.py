import random
# ■


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

matrix = [[None for y in range(altura)] for x in range(largura)]


def print_matrix():
	for x in matrix:
		for y in x:
			if len(str(y)) == 1 and y != "■":
				print(" ", y, sep="", end="")
			else:
				print(y, end="")
		# print("%02d" % y, end="")
		print("")


def gera_obstaculos(n):
	for hue1 in range(n):
		x = random.randint(0, altura)
		y = random.randint(0, largura)
		if random.getrandbits(1):
			# horizontal
			for hue2 in range(random.randint(3, 10)):
				if y < largura:
					matrix[x][y] = "■"
					y += 1
				else:
					break
		else:
			# vertical
			for hue2 in range(random.randint(3, 10)):
				if x < altura:
					matrix[x][y] = "■"
					x += 1
				else:
					break


def esta_cheio():
	if matrix[0][0] == None:
		return False
	elif matrix[0][largura-1] == None:
		return False
	elif matrix[altura-1][0] == None:
		return False
	elif matrix[altura-1][largura-1] == None:
		return False
	else:
		for x in matrix:
			for y in x:
				if y == None:
					return False
	return True


x = random.randint(0, altura)
y = random.randint(0, largura)

posicoes1 = [[x, y]]
posicoes2 = []

matrix[x][y] = 0
numero_atual = 0


def propaga(lista_posicoes_a, lista_posicoes_b):
	global numero_atual, posicoes1, posicoes2
	for x, y in lista_posicoes_a:
		# esquerda
		if y > 0 and matrix[x][y - 1] == None:
			matrix[x][y - 1] = numero_atual + 1
			lista_posicoes_b.append([x, y-1])
		# cima
		if x > 0 and matrix[x - 1][y] == None:
			matrix[x - 1][y] = numero_atual + 1
			lista_posicoes_b.append([x - 1, y])
		# direita
		if y <= largura - 2 and matrix[x][y + 1] == None:
			matrix[x][y + 1] = numero_atual + 1
			lista_posicoes_b.append([x, y + 1])
		# baixo
		if x <= altura - 2 and matrix[x + 1][y] == None:
			matrix[x + 1][y] = numero_atual + 1
			lista_posicoes_b.append([x + 1, y])

	numero_atual += 1
	lista_posicoes_a = []


def anda(x, y):
	# criar condição pra quando estiver encostado na parede
	global endx, endy

	menor = matrix[x-1][y-1]
	matrix[x][y] = "x"
	novox = x
	novoy = y

	# cima
	if type(matrix[x-1][y]) == int and matrix[x-1][y] < menor:
		menor = matrix[x - 1][y]
		novox -= 1
	# cima direita
	if type(matrix[x-1][y+1]) == int and matrix[x-1][y+1] < menor:
		menor = matrix[x - 1][y+1]
		novox -= 1
		novoy += 1
	# direita
	if type(matrix[x][y+1]) == int and matrix[x][y+1] < menor:
		menor = matrix[x][y+1]
		novoy += 1
	# baixo direita
	if type(matrix[x+1][y+1]) == int and matrix[x+1][y+1] < menor:
		menor = matrix[x+1][y+1]
		novox += 1
		novoy += 1
	# baixo
	if type(matrix[x+1][y]) == int and matrix[x+1][y] < menor:
		menor = matrix[x + 1][y]
		novox += 1
	# baixo esquerda
	if type(matrix[x+1][y-1]) == int and matrix[x+1][y-1] < menor:
		menor = matrix[x + 1][y-1]
		novox += 1
		novoy -= 1
	# esquerda
	if type(matrix[x][y-1]) == int and matrix[x][y-1] < menor:
		menor = matrix[x][y-1]
		novoy -= 1

	endx = novox
	endy = novoy


gera_obstaculos(10)

while not esta_cheio():
	propaga(posicoes1, posicoes2)
	propaga(posicoes2, posicoes1)

endx = random.randint(0, altura)
endy = random.randint(0, largura)

while matrix[endx][endy] != 0:
	anda(endx, endy)

print_matrix()
