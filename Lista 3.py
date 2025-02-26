import numpy as np
import random as rd

print('Exercicio 1')
x = np.ones(8)
y = np.random.randint(0, 10, 8)

print(f'Array de 1: {x}')
print(f'Array de valores aleatórios: {y}')

soma = x + y
print(f'Soma dos Arrays: {soma}')

print(soma.sum())

if soma.sum() >= 40:
    print(soma.reshape(4,2))
    print(' ')

else:
    print(soma.reshape(2,4))
    print(' ')

print('Exercicio 2')

arr = np.arange(0, 50, 2)

print(arr)

arr2 = np.arange(100, 49, -2)

print(arr2)

arrconca = np.concatenate((arr, arr2))
print(np.sort(arrconca))

print(' ')

print('Exercicio 3')

matrzero = np.zeros((2,2), dtype=int)

row = rd.randint(0, 1)
column = rd.randint(0, 1)

matrzero[row][column] = 1

row = int(input('Escolha uma linha, 0 ou 1 '))
column = int(input('Escolha uma coluna, 0 ou 1 '))

if matrzero[row][column] == 1:
    print('Congrulations! You beat the game!!\n')

else:
    print('Game Over! :( Try Again\n')

print('Exercicio 4')

rows = rd.randint(2, 100)
columns = rd.randint(2, 100)
matrix = np.random.randint(2, 10, (rows, columns))

resultado = rows*columns

if resultado % 2 == 0:
    print('Seria um vetor par\n')
else:
    print('Seria um vetor impar\n')

print('Exercicio 5')

np.random.seed(100)
matrix = np.random.randint(0, 50, (2,2))

matrix_row = np.mean(matrix, axis=1)
matrix_column = np.mean(matrix, axis=0)

print(f'Média das linhas:{matrix_row}')
print(f'Média das colunas:{matrix_column}')

maior_row = np.max(matrix_row)
maior_column = np.max(matrix_column)

print(f'Maior média das linhas:{maior_row}')
print(f'Maior média das colunas:{maior_column}')

valores, contagens = np.unique(matrix, return_counts=True)

ocorrencias = dict(zip(valores, contagens))

for num, qtd in ocorrencias.items():
    print(f'O {num} apareceu {qtd} vezes')

numeros_2x = [num for num, qtd in ocorrencias.items() if qtd == 2]

print(f'Números que aparecem exatamente 2 vezes: {numeros_2x}')