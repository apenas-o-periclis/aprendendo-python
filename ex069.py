#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
mais_18 = homens = mulheres_20 = 0

while True:
    sexo = str(input('Qual seu sexo? [F/M] ')).strip().lower()[0]
    while sexo not in 'MmFf':
        print('Opção inválida, tente novamente')
        sexo = str(input('Qual seu sexo? [F/M]')).strip().lower()[0]
    idade = int(input('Quantos anos você tem? '))
    if idade >= 18:
        mais_18 += 1
    if idade < 20 and sexo == 'f':
        mulheres_20 += 1
    if sexo == 'm':
        homens += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    while continuar not  in 'sn':
        print('Opção inválida, tente novamente')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'{mais_18} pessoa tem mais de 18. {mulheres_20} mulheres tem menos de 20 anos. {homens} homens foram cadastrados.')