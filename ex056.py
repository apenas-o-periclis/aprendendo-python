#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from datetime import date
todas_idades = 0
maior_idade = 0 
menos_20 = 0
for c in range(1,5):
    print(f'''                 Analise completa do grupo
          {'-' * 15} {c}° Pessoa {'-' * 15}''')
    nome = str(input(f'Digite o nome da {c}° pessoa: ')).strip().lower()
    idd = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    sexo = int(input('''Selecione o sexo da {c}° pessoa: 
               [ 1 ] para masculino
               [ 2 ] para feminino
                     Sua opção: '''))
    idade = date.today().year - idd
    todas_idades = todas_idades + idade
    if sexo == 1:
        if c == 1:
            maior_idade = idade
            nome_homem = nome
        else:
            if idade > maior_idade:
                maior_idade = idade
                nome_homem = nome
    if sexo == 2:
        if idade < 20:
            menos_20 = menos_20 + 1
    
media_idade = todas_idades / c

print(f'A média de idade do grupo foi {media_idade}')
print(f'O nome do homem mais velho é {nome_homem}')
if menos_20 == 1:
    print('Foi reconhecida apenas 1 mulher com menos de 20 anos.')
else:
    print(f'O numero de mulheres com menos de 20 anos é {menos_20}')