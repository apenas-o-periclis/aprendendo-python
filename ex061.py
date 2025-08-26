#refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while

termo = float(input('Digite o primeiro termo: '))
razão = float(input('Digite a razão da PA: '))
resultado = termo
c = 1
print(f'O primeiro termo foi {termo} seguido de: ', end='')
while c !=10:
    resultado = resultado + razão
    c = c + 1 
    if c <10:
        print(f'{resultado} -> ', end='')
    else:
        print(resultado)