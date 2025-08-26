#faça um programa que leia o sexo de uma pessoa, mas so aceite 'm' ou 'f'. Caso esteja errado, peça digitação novamente até ter um valor correto
f = 'f'
m = 'm' 
sexo = str(input('Qual seu sexo: [f/m]')).strip().lower()[0]
while sexo not in ('f', 'm'):
    print('Opção inválida, tente novamente.')
    sexo = str(input('Qual seu sexo: [f/m]')).strip().lower()[0]
print(f'Sexo {sexo} registrado com sucesso')