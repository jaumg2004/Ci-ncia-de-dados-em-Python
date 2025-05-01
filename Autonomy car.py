import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
import pandas as pd

# Carregando o CSV enviado (nome do carro como índice)
mtcars = pd.read_csv(r'C:\Users\Jaum\Downloads\mt_cars_augmented.csv', index_col=0)

# Features e alvo
X = mtcars[['mpg', 'hp']].values
y = mtcars['cyl'].values

# Modelo KNN
knn = KNeighborsClassifier(n_neighbors=4)
modelo = knn.fit(X, y)

# Avaliação do modelo
y_prev = modelo.predict(X)
print(f'Acurácia: {accuracy_score(y, y_prev):.2f}')
print(f'Precisão: {precision_score(y, y_prev, average="weighted"):.2f}')
print(f'Recall: {recall_score(y, y_prev, average="weighted"):.2f}')
print(f'F1 Score: {f1_score(y, y_prev, average="weighted"):.2f}')
print('Matriz de confusão:\n', confusion_matrix(y, y_prev))

# Entrada do usuário
print('\nDigite os valores para previsão:')
mpg = float(input("Milhas por galão (mpg): "))
hp = int(input("Cavalos de potência (hp): "))
new_data = np.array([[mpg, hp]])
previsao = modelo.predict(new_data)
print(f'\nPrevisão de cilindros: {previsao[0]}')

# Encontrando carro mais próximo
distancia, indices = modelo.kneighbors(new_data)
carro_mais_proximo = mtcars.iloc[indices[0][0]]
nome_carro = mtcars.index[indices[0][0]]
print(f'\nCarro mais próximo: {nome_carro}')
print(f'Detalhes: MPG = {carro_mais_proximo["mpg"]}, HP = {carro_mais_proximo["hp"]}, Cilindros = {carro_mais_proximo["cyl"]}')
print(f'Distância até o novo ponto: {distancia[0][0]:.4f}')

# Plot
plt.figure(figsize=(10, 6))

# Dados do conjunto
for classe in np.unique(y):
    plt.scatter(X[y == classe, 0], X[y == classe, 1], label=f'{classe} cilindros')

# Novo ponto
plt.scatter(new_data[0][0], new_data[0][1], color='black', marker='X', s=200,
            label=f'Novo dado (previsto): {previsao[0]}')

# Carro mais próximo
plt.scatter(carro_mais_proximo['mpg'], carro_mais_proximo['hp'], color='red', marker='o', s=150,
            label='Carro mais próximo')
plt.annotate(f"{nome_carro}\nMPG: {carro_mais_proximo['mpg']}, HP: {carro_mais_proximo['hp']}, CYL: {carro_mais_proximo['cyl']}",
             xy=(carro_mais_proximo['mpg'], carro_mais_proximo['hp']),
             xytext=(carro_mais_proximo['mpg'] + 1, carro_mais_proximo['hp'] + 5),
             arrowprops=dict(facecolor='red', arrowstyle="->"),
             fontsize=9, backgroundcolor='white')

# Título e eixos
plt.title('Classificação com KNN - Previsão de cilindros')
plt.xlabel('Milhas por galão (mpg)')
plt.ylabel('Cavalos de potência (hp)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
