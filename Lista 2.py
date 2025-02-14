print('Exercicio 1')

vencedores = ['Bayner de Munique', 'Real Madrid', 'PSG', 'Barcelona', 'Manchester City']
print(vencedores[:3])
print(vencedores[3:])
print(sorted(vencedores))
print(vencedores.index('Barcelona'))
print('')

print('Exercicio 2')
loja1 = {'Samsung Galaxy S23', 'iPhone 14', 'Google Pixel 7', 'Xiaomi 13', 'OnePlus 11'}
loja2 = {'iPhone 14', 'Samsung Galaxy A54', 'Xiaomi Mi 13', 'OnePlus 9', 'Realme 11 Pro', 'Oppo Reno 8 Pro'}
print(f'Loja 1: {loja1}')
print(f'Loja 2: {loja2}')
print(f'Smartphones diponiveis: {loja1 | loja2}')
print(f'Smartphones que ambas possuem: {loja1 & loja2}\n')

print('Exercicio 3')
nome = input('Digite o nome do aluno: ')
media = float(input('Qual a media do aluno? '))

dados = {'nome':nome, 'media':media}
if dados['media'] >= 50:
    print('AP\n')
else:
    print('RP\n')

print(f'Nome do aluno: {dados['nome']}')
print(f'Média do aluno: {dados['media']}')

print('Exercicio 4')
nomes = []
pesos = []

for _ in range(3):
    nomes.append(input('Digite o nome de uma pessoa: '))
    pesos.append(float(input('Digite o seu peso: ')))

print(f'Nome da pessoa mais gorda: {nomes[pesos.index(max(pesos))]}')
print(f'Nome da pessoa mais leve: {nomes[pesos.index(min(pesos))]}\n')

print('Exercicio 5')
total_idade = 0
mulheres_menor_20 = 0
total_pessoas = int(input('Digite o número de pessoas: '))

for i in range(total_pessoas):
    nome = input(f'Nome da pessoa {i+1}: ')
    idade = int(input(f'Idade de {nome}: '))
    sexo = input(f'Sexo de {nome} (M/F): ').strip().upper()

    total_idade += idade

    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1

media_idade = total_idade / total_pessoas if total_pessoas > 0 else 0

print(f'A média de idade do grupo é: {media_idade:.2f} anos')
print(f'Número de mulheres com menos de 20 anos: {mulheres_menor_20}')
