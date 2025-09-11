#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:   
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
tot = mais_1000 = 0
nome = str(input('Qual o nome do produto: '))
valor = float(input('Qual o valor do produto: R$'))
produtob = valor
maisb = nome
while True:
    tot += valor
    if valor > 1000:
        mais_1000 += 1
    if valor < produtob:
        produtob = valor
        maisb = nome
    continuar = str(input('Quer continuar: [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
    nome = str(input('Qual o nome do produto: '))
    valor = float(input('Qual o valor do produto: R$'))
print(f'R${tot:.2f} foi o valor total. {mais_1000} produtos custam mais de R$1000. {maisb} é o produtor mais barato.')
