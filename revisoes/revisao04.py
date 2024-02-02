import numpy as np
import random
import matplotlib.pyplot as plt

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

def main():
  limite_passos = 500
  origem = (200, 200)
  destino = (0, 0)
  numero_simulacoes = 1000
  
  matriz_result = np.zeros((400,400),dtype=np.int32)
  for i in range(numero_simulacoes):
    matriz_result = realizar_caminha(matriz_result, limite_passos, origem, destino)
    
  probabilidade_sucesso = (matriz_result[destino]/numero_simulacoes)*100
  print(f"Probabilidade de sucesso: {probabilidade_sucesso}%")
   
  show_heat_map(matriz_result)
  show_gray_map(matriz_result)
  
def show_heat_map(array: np.ndarray):
  plt.figure()
  plt.imshow(array, origin='lower', cmap='hot')
  plt.colorbar()
  plt.show()
    
def show_gray_map(array: np.ndarray):
  intensidade = 1
  plt.figure()
  plt.imshow(array, origin='lower', cmap='gray', vmin=intensidade, vmax=intensidade)
  plt.colorbar()
  plt.show()

if __name__ == '__main__':
  main()