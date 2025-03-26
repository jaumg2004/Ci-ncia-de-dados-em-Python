import pandas as pd
import os
import numpy as np

data = pd.read_csv(r'C:\Users\Jaum\Downloads\paises.csv', delimiter=';')

print('Exercício 1')
oceania = data[data['Region'] == 'OCEANIA                            ']
print(f'A oceania possui {oceania.count()['Country']} ao todo, e eles são: {', '.join(oceania['Country'])}\n')

print('Exercício 2')

population = data['Population']
region = data['Region']
country = data['Country']
print(f'O país com a maior população é a {country[population.idxmax()]} da {region[population.idxmax()]}\n')

print('Exercício 3')

group_region = data.groupby('Region')
print(group_region['Literacy (%)'].mean())

print('\nExercício 4')

noCoast = data[data['Coastline (coast/area ratio)'] == 0]
diretorio = os.path.join(r'C:\Users\Jaum\Downloads', 'noCoast.csv')
noCoast.to_csv(diretorio, sep=';')
print(f'Arquivo salvo em: {diretorio}\n')

print('Exercício 5')
def helphumanitary(x:float) -> str:
    return 'Balanced' if x < 9 else 'Urgent'

seriesDeathrate = data['Deathrate'].apply(helphumanitary)
data['Humanitary Help'] = np.round(seriesDeathrate)
print(data)