#JONATA

def posicao_eh_valida(matriz, tamanho, orientacao, x, y):
    if orientacao == 'horizontal':
        # Verifica se existem partes de navio nas posições novas ou adjacente a elas
        for i in range(y-1, y+2):
            if i < 0 or i >= len(matriz):
                continue
            for j in range(x-1, x+tamanho+1):
                if j < 0 or j >= len(matriz):
                    continue
                if matriz[i][j] == 'N':
                    #print('existem pedaços de navio adjacentes')
                    return False
    if orientacao == 'vertical':
        # Verifica se existem partes de navio nas posições novas ou adjacente a elas
        for i in range(y-1, y+tamanho+1):
            if i < 0 or i >= len(matriz):
                continue
            for j in range(x-1, x+2):
                if j < 0 or j >= len(matriz):
                    continue
                if matriz[i][j] == 'N':
                    #print('existem pedaços de navio adjacentes')
                    return False
    return True


