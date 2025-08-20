#refaca o desafio 35, acrescentando o recurso de mostrar que tipo de etriangulo sera formado:
#- Equilatero:Todos os lados igual
#- isosceles:Dois lados iguais
#- Escaleno:Todos os lados diferentes

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and r1 == r2 == r3:
    print('Essas retas PODEM formar um triângulo, e ele seria um triângulo EQUILÁTERO.')
elif r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 and r1 == r2 !=r3 or r1 == r3 != r2 or r2 == r3 !=r1:
    print('Essas retas PODEM formar um triângulo, e ele seria ISOSCELES.')
elif r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 and r1 !=r2 !=r3:
    print('Essas retas PODEM formar um triângulo e ele seria ESCALENO.')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')