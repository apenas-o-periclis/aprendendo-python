#Crie um programa que leia vários números inteiros pelo teclado, o programa so vai parar quando o usuário digitar o valor 999, que é a condição de parada, no final, mostre quantos numeros foram digitados, e qual foi a soma entre eles (desconsiderando o flag)
soma = 0
cont = 0
while True:
    num = int(input('Digite um número para somar (Digite 999 para parar.): '))
    if num == 999:
        break #Lembre-se que o while roda os códigos 'seguidos', logo o while vai desconsiderar tudo que estiver abaixo do break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}.')