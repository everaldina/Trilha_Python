import numpy as np
import random

def realizar_caminha(matrix, limite_passos, origem, destino):
    passos = 0
    posicao_atual = origem
    altura, largura = matrix.shape
    while passos < limite_passos:
        if posicao_atual == destino:
            break
        
        # cria uma lista com as possíveis escolhas
        escolhas = ['cima', 'baixo', 'esquerda', 'direita']
        if posicao_atual[0] == 0:
            escolhas.remove('cima')
        elif posicao_atual[0] == altura - 1:
            escolhas.remove('baixo')
        
        if posicao_atual[1] == 0:
            escolhas.remove('esquerda')
        elif posicao_atual[1] == largura - 1:
            escolhas.remove('direita')
        
        
        # escolhe uma direção
        direcao = random.choice(escolhas)
        
        match direcao:
            case 'cima':
                posicao_atual = (posicao_atual[0] - 1, posicao_atual[1])
            case 'baixo':
                posicao_atual = (posicao_atual[0] + 1, posicao_atual[1])
            case 'esquerda':
                posicao_atual = (posicao_atual[0], posicao_atual[1] - 1)
            case 'direita':
                posicao_atual = (posicao_atual[0], posicao_atual[1] + 1)
        
        passos += 1
        matrix[posicao_atual] += 1
    return matrix


def simular_trajetoria():
    # Tamanho da matriz
    tamanho_matriz = 400

    # Posição inicial do bar
    i, j = 200, 200

    # Inicializar a 
    visitas = np.zeros((400, 400))

    # Número máximo de passos por simulação
    max_passos = 500


  
