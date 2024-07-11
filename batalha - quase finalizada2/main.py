import random
from modulos import matriz as mt

tropas = int(input('Digite de 1 a 6 quantos navios cada jogador terá: '))

opcao = input(
    'Deseja iniciar um novo jogo (N) ou carregar um jogo salvo (C)? ')

if opcao.lower() == 'n':
    player1 = mt.criar_tabuleiro(tropas)
    frota1 = tropas
    player2 = mt.criar_tabuleiro(tropas)
    frota2 = tropas
else:
    arquivo = input('Digite o nome do arquivo de salvamento: ')
    player1 = mt.carregar_jogo(f'{arquivo}_player1.txt')
    player2 = mt.carregar_jogo(f'{arquivo}_player2.txt')

print('player1:')
mt.imprimir_mapa(player1)
print('player2:')
mt.imprimir_mapa(player2)
jogador_atual = 1

while True:
    if jogador_atual == 1:
        print('Jogador 1:')
        mt.imprimir_mapa(mt.matrizVisual2)
        while True:
            linha = input('Digite a linha do tiro: ')
            if linha.isalpha() and len(linha) == 1 and 'A' <= linha.upper() <= 'H':
                break
            print('Entrada inválida! Digite uma letra de A a H.')

        coluna = int(input('Digite a coluna do tiro: '))
        if player2[ord(linha.upper()) - ord('A')][coluna] == 'N':
            print('FOGO!')
            mt.matrizVisual2[ord(linha.upper()) - ord('A')][coluna] = 'F'
            player2[ord(linha.upper()) - ord('A')][coluna] = 'F'
            print('Você destruiu uma parte de um barco!')
            if mt.verificar_vitoria(player2):
                print('Jogador 1 venceu!')
                break
        else:
            print('ÁGUA!')
            mt.matrizVisual1[ord(linha.upper()) - ord('A')][coluna] = 'A'
            jogador_atual = 2
    else:
        print('Jogador 2:')
        mt.imprimir_mapa(mt.matrizVisual1)
        while True:
            linha = input('Digite a linha do tiro: ')
            if linha.isalpha() and len(linha) == 1 and 'A' <= linha.upper() <= 'H':
                break
            print('Entrada inválida! Digite uma letra de A a H.')

        coluna = int(input('Digite a coluna do tiro: '))
        if player1[ord(linha.upper()) - ord('A')][coluna] == 'N':
            print('FOGO!')
            mt.matrizVisual1[ord(linha.upper()) - ord('A')][coluna] = 'F'
            player1[ord(linha.upper()) - ord('A')][coluna] = 'F'
            print('Você destruiu uma parte de um barco!')
            if mt.verificar_vitoria(player1):
                print('Jogador 2 venceu!')
                break
        else:
            print('ÁGUA!')
            mt.matrizVisual1[ord(linha.upper()) - ord('A')][coluna] = 'A'
            jogador_atual = 1

    opcao = input('Deseja salvar o jogo? (S/N): ')
    if opcao.lower() == 's':
        arquivo = input('Digite o nome do arquivo de salvamento: ')
        mt.salvar_jogo(player1, f'{arquivo}_player1.txt')
        mt.salvar_jogo(player2, f'{arquivo}_player2.txt')
