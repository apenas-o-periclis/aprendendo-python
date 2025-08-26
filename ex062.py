#melhor o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos, o programa encerra quando ele disser que quer mostrar 0 termos
termo = float(input('Digite o primeiro termo da PA: '))
razão = float(input('Digite a razão da PA: '))
resultado = termo
c = 2
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while c <= total:
        print(f'{resultado} -> ', end='')
        resultado = resultado + razão
        c = c + 1
    print(resultado)
    print('Pausa...')
    mais = int(input('Quantos termos a mais você quer digitar? (Digite 0 para encerrar): '))
print(f'Progressão finalizada com {total} termos.')
print('FIM')