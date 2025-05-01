import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data_paises = pd.read_csv(r'C:\Users\Jaum\Downloads\paises.csv', delimiter=';')

print('Exercício 1')
northern_america = data_paises[data_paises['Region'] == 'NORTHERN AMERICA                   ']
na_mortalidade = northern_america['Deathrate'].to_list()
na_natalidade = northern_america['Birthrate'].to_list()
na_paises = northern_america['Country'].to_list()

plt.figure(figsize=(12, 6))
plt.title('Exercício 1 - Taxas de Natalidade e Mortalidade na América do Norte')
plt.plot(na_paises, na_mortalidade, 'r--', label='Mortalidade')
plt.plot(na_paises, na_natalidade, 'b-', label='Natalidade')
plt.xticks(rotation=45)
plt.xlabel('Países')
plt.ylabel('Taxas (por mil habitantes)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print('Exercício 2')

data_space = pd.read_csv(r'C:\Users\Jaum\Downloads\space.csv', delimiter=';')
usa_missions = len(data_space[data_space['Location'].str.contains('USA', case=False, na=False)])
china_missions = len(data_space[data_space['Location'].str.contains('China', case=False, na=False)])

plt.bar(['China', 'USA'], [china_missions, usa_missions], color='red')
plt.title('Exercício 2 - Quantidade de empresas dos EUA e China')
plt.show()

print('Exercício 3')
roscosmos = data_space[data_space['Company Name'].str.contains('Roscosmos', case=False, na=False)]
success_roscosmos = len(roscosmos[roscosmos['Status Mission'].str.contains('Success', case=False, na=False)])/len(roscosmos)
failure_roscosmos = len(roscosmos[roscosmos['Status Mission'].str.contains('Failure', case=False, na=False)])/len(roscosmos)
plt.pie(x=[success_roscosmos, failure_roscosmos], labels=['% de missões sucedidas da Roscosmos', '% de missões fracasadas da Roscosmos'], autopct='%1.1f%%')
plt.title('Exercício 3 - Missões da Roscosmos')
plt.show()