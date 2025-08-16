import random
a1 = input('Qual nome do primeiro aluno: ')
a2 = input('Qual nome do segundo aluno: ')
a3 = input('Qual nome do terceiro aluno: ')
a4 = input('Qual o nome do quarto aluno: ')
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print('a ordem de apresentacao da lista sera')
print('-' * 40)
print(alunos)
print('-' * 40)