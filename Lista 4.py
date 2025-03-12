import numpy as np

data = np.loadtxt(r'C:\Users\Jaum\Downloads\space.csv', delimiter=';', dtype='str', encoding='utf-8')

print('Exercício 1')
print(f'Porcentagem de missões que foram um sucesso: {np.mean(data[1:, 7] == 'Success') * 100:.2f}%\n')

print('Exercício 2')
cost_mission_column = data[1:, 6].astype(float)
print(f'Média do valor das missões em milhões: {np.mean(cost_mission_column[cost_mission_column > 0]):.2f}\n')

print('Exercício 3')
location_USA = np.char.find(data[:, 2], 'USA')
tam = np.sum(location_USA != -1)
print(f'Quantidade de missões realizadas nos EUA: {tam}\n')

print('Exercício 4')
details_column = data[1:, 4]
company_column = data[1:, 1]
space_x = np.where(company_column == 'SpaceX')
space_x_cost = cost_mission_column[space_x]
space_x_details = details_column[space_x]
details_cost = "; ".join(space_x_details[np.where(space_x_cost == max(space_x_cost))])
print(f'As missões mais caras da SpaceX foram: {details_cost}\n')

print('Exercício 5')
company = np.unique(company_column)
company_count = [np.sum(company_column == comp) for comp in company]
print('Empresas que já realizaram missões no espaço e quantidade de missões\n')
for comp, count in zip(company, company_count):
    print(f'Nome: {comp} ; Missões: {count}')






