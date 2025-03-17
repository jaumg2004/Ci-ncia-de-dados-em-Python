import numpy as np

data = np.loadtxt(r'C:\Users\Jaum\Downloads\paises.csv', delimiter=';',dtype=str,encoding='utf-8')

print('Exercício 1')

country = data[1:, 0]
region = data[1:, 1]
population = data[1:, 2]
area = data[1:, 3]

for count, reg, pop, area in zip(country, region, population, area):
    print(f'País: {count}; Região: {reg}; População: {pop}; Área: {area}')

print('\nExercício 2')

diferent_region = np.unique(region)
print(f'O mundo tem {diferent_region.size}, sendo elas: {",".join(diferent_region)}\n')

print('Exercício 3')

literacy = data[1:, 9].astype(float)
print(f'A taxa média de alfabetização do planeta é: {np.mean(literacy):.2f}%\n')

print('Exercício 4')
north_america = region[region == 'NORTHERN AMERICA                   ']
print(f'{north_america.size} países são da América do Norte\n')

print('Exercício 5')

gdp = data[1:, 8].astype(float)
gdp_caribe_latam = gdp[region == 'LATIN AMER. & CARIB    ']
pais_max_gdp = "".join(country[region == 'LATIN AMER. & CARIB    '][gdp_caribe_latam == max(gdp_caribe_latam)])
print(f'O país do Caribe e da América Latina com a maior renda per capita é o {pais_max_gdp}')