import numpy as np

data = np.loadtxt(r'C:\Users\Jaum\Downloads\social_media.csv', delimiter=';',dtype=str,encoding='utf-8')

print('Exercício 1')
brazil = np.sum(data[1:, 4] == 'Brazil')
print(f'{brazil} posts são do Brasil\n')

print('Exercício 2')
education = np.mean(data[1:, 2] == 'Education') * 100
print(f'{education:.2f}% usaram a hashtag Education\n')

print('Exercício 3')
views = data[1:, 5].astype(float)
likes = data[1:, 6].astype(float)
instagram = np.where(data[1:, 1] == 'Instagram')
likes_insta = np.mean(likes[instagram])
views_insta = np.mean(views[instagram])
insta_likes_views = {'views':likes_insta, 'likes':views_insta}
print(f'A média de views e likes do Instagram são, respectivamente: {insta_likes_views['views']:.2f} e {insta_likes_views['likes']:.2f}\n')

print('Exercício 4')
plataform, posts = np.unique(data[1:, 1], return_counts=True)
plataform_com_mais_posts = plataform[posts == max(posts)]
print(f'A plataforma com mais posts é o {"".join(plataform_com_mais_posts)} com {max(posts)} posts\n')

print('Exercício 5')
region = data[1:, 4]
region_more_likes = region[likes == max(likes)]
print(f'A região com maior número de likes é a {"".join(region_more_likes)}')