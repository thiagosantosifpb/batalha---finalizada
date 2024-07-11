import random

matrizVisual1 = [['x' for _ in range(8)] for _ in range(8)]
matrizVisual2 = [['x' for _ in range(8)] for _ in range(8)]

def imprimir_mapa(matriz):
    print('  0 1 2 3 4 5 6 7')
    for i in range(8):
        print(chr(ord('A') + i), ' '.join(matriz[i]))

def criar_tabuleiro(tropas):
    matriz = [['x' for _ in range(8)] for _ in range(8)]
    tamanho_navios = []
    for i in range(tropas):
        tamanho_navios.append(random.randint(2, 4))
    for tamanho in tamanho_navios:
        while True:
            orientacao = random.choice(['horizontal', 'vertical'])
            if orientacao == 'horizontal':
                x = random.randint(0, 8 - tamanho)
                y = random.randint(0, 7)
                if posicao_eh_valida(matriz, tamanho, orientacao, x, y):
                    for i in range(x, x + tamanho):
                        matriz[y][i] = 'N'
                    break
            else:
                x = random.randint(0, 7)
                y = random.randint(0, 8 - tamanho)
                if posicao_eh_valida(matriz, tamanho, orientacao, x, y):
                    for i in range(y, y + tamanho):
                        matriz[i][x] = 'N'
                    break
    return matriz

def posicao_eh_valida(matriz, tamanho, orientacao, x, y):
    if orientacao == 'horizontal':
        for i in range(y-1, y+2):
            if i < 0 or i >= len(matriz):
                continue
            for j in range(x-1, x+tamanho+1):
                if j < 0 or j >= len(matriz):
                    continue
                if matriz[i][j] == 'N':
                    return False
    if orientacao == 'vertical':
        for i in range(y-1, y+tamanho+1):
            if i < 0 or i >= len(matriz):
                continue
            for j in range(x-1, x+2):
                if j < 0 or j >= len(matriz):
                    continue
                if matriz[i][j] == 'N':
                    return False
    return True

def verificar_destruicao(matriz, linha, coluna):
    tamanho_barco = 0

    i = coluna + 1
    while i < 8 and matriz[linha][i] == 'F':
        tamanho_barco += 1
        i += 1

    i = coluna - 1
    while i >= 0 and matriz[linha][i] == 'F':
        tamanho_barco += 1
        i -= 1

    i = linha + 1
    while i < 8 and matriz[i][coluna] == 'F':
        tamanho_barco += 1
        i += 1

    i = linha - 1
    while i >= 0 and matriz[i][coluna] == 'F':
        tamanho_barco += 1
        i -= 1

    return tamanho_barco == 0

def verificar_vitoria(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True


#funções para salvamento 
def salvar_jogo(tabuleiro, arquivo):
    with open(arquivo, 'w') as file:
        for linha in tabuleiro:
            file.write(' '.join(linha) + '\n')

def carregar_jogo(arquivo):
    tabuleiro = []
    with open(arquivo, 'r') as file:
        for linha in file:
            tabuleiro.append(linha.strip().split(' '))
    return tabuleiro