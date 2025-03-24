import pandas as pd
import numpy as np

print('Exercício 1')

seriesAno1 = pd.Series({'Java':16.25, 'C':16.04, 'Python':9.85})
seriesAno2 = pd.Series({'Java':16.21, 'Python':12.12, 'C':11.68})
print(seriesAno1)
print(seriesAno2, '\n')

print('Exercício 2')
print(seriesAno1 + seriesAno2, '\n')

print('Exercício 3')
seriesAno_dif = seriesAno1 - seriesAno2
print(seriesAno_dif, '\n')

print('Exercício 4')
print(', '.join(seriesAno_dif[seriesAno_dif > 0].index.tolist()), '\n')

print('Exercício 5')
series2Anos = seriesAno2 + 2*seriesAno_dif
print(series2Anos.idxmax())

print('Exercício 6')

df = pd.DataFrame(index=['A', 'B', 'C', 'D', 'E'],
                  columns=['W', 'X', 'Y', 'Z'],
                  data=np.random.randint(1, 50, [5, 4]))

print(df['X'][df['X'] < 30].mean(), '\n')

print('Exercício 7')
df_D = df.loc[['D'],['W', 'X', 'Y', 'Z']]
df_E = df.iloc[4, :]
print(df_D.mean(axis=1).values[0])
print(df_E.sum(), '\n')

print('Exercício 8')

Data = df.iloc[0:5:2, 1:3]
for index in range(Data.shape[0]):
     print(Data.iloc[index].sum())

print(' ')

for column in range(Data.shape[1]):
    print(Data.iloc[:, column].sum())
