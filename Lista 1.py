import random
import math

print('Exercicio 1')

nome = input("Digite o seu nome completo: ")

print(nome.upper())
print(nome.lower())
print('Tamanho do seu nome:', len(nome))
palavras = nome.split()
if len(palavras) > 1:
    palavras[-1] = "do Inatel"
nome=" ".join(palavras)
print(nome,'\n')

print('Exercicio 2')

numero = int(input('Escolha um número: '))
for i in range(11):
    resultado = i*numero
    print(i,'x',numero,'=',resultado)
print('\n')

print('Exercicio 3')

sexo = input()

while sexo != 'M' and sexo != 'F':
    sexo = input()

print('\n')

print('Exercicio 4')

distancia = float(input("Digite a distancia da viagem em km: "))

if distancia > 200:
    valor = 0.45*distancia
    print(f'Preço da passagem: R${valor}\n')

else:
    valor = 0.5*distancia
    print(f'Preço da passagem: R${valor}\n')

print('Exercicio 5')

numero = random.randint(1000, 9999)
print(f'Milhar: {numero//1000}')
print(f'Centena: {(numero//100)%10}')
print(f'Dezena: {(numero//10)%10}')
print(f'Unidade: {numero%10}\n')

print('Exercicio 6')

numero = float(input('Entre com um número decimal: '))

print(f'Raíz quadrada: {numero**(0.5):.2f}')
print(f'Sua parte inteira: {int(numero)}')
print(f'Função teto: {math.ceil(numero)}')
print(f'Função chão: {math.floor(numero)}')
