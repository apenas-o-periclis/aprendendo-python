#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida
#- media abaixo de 5.0:REPROVADO
#- media entre 5.0 e 6.9:RECUPERAÇÃO
#- media 7.0 ou superior:APROVADO

n1 = float(input('digite sua nota da prova de portugues:'))
n2 = float(input('digite sua nota da prova de ingles'))
m = (n1 + n2) / 2 
print(f'sua media foi {m}.')
if m <5.0:
    print('voce foi reprovado!') 
elif m >5 and m <7:
    print('voce ficou de recuperação!')
else:
    print('voce foi aprovado!')