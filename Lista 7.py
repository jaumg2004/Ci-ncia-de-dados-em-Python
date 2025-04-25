import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
import pandas as pd

# Carregando os dados
mtcars = pd.read_csv(r'C:\Users\Jaum\Desktop\download\download\3.Algoritmos de Machine Learning\mt_cars.csv')

# Definindo as features e o target
X = mtcars[['mpg','hp']].values
y = mtcars['cyl'].values

# Treinando o modelo
knn = KNeighborsClassifier(n_neighbors=3)
modelo = knn.fit(X, y)

# Fazendo a previsão com os dados de treino
y_prev = modelo.predict(X)

# Métricas
accuracy = accuracy_score(y, y_prev)
precision = precision_score(y, y_prev, average='weighted')
recall = recall_score(y, y_prev, average='weighted')
f1 = f1_score(y, y_prev, average='weighted')
cm = confusion_matrix(y, y_prev)

print(f'Acurácia: {accuracy:.2f}, Precisão: {precision:.2f}, Recall: {recall:.2f}, F1: {f1:.2f}')
print('Matriz de confusão:\n', cm)

# Previsão para novo dado
new_data = np.array([[19.3, 105]])
previsao = modelo.predict(new_data)
print(f'Previsão: {previsao}')

distancia, indices = modelo.kneighbors(new_data)
print(f'Distância: {distancia}')
print(f'Índices: {indices}')

print(mtcars.loc[indices[0], ['cyl', 'mpg', 'hp']])

# Plot
plt.figure(figsize=(10, 6))

# Plotando os pontos do dataset original coloridos pela classe
for classe in np.unique(y):
    plt.scatter(X[y == classe, 0], X[y == classe, 1], label=f'{classe} cilindros')

# Plotando o novo ponto previsto
plt.scatter(new_data[0][0], new_data[0][1], color='black', marker='X', s=200, label='Novo dado (previsto)')

# Título e legendas
plt.title('Classificação com KNN - Previsão de cilindros')
plt.xlabel('mpg')
plt.ylabel('hp')
plt.legend()
plt.grid(True)
plt.show()
