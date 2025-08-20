num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] conversor para BINÁRIO
[ 2 ] conversor para OCTAL
[ 3 ] conversor para HEXADECIMAL''')
opc = int(input('Sua opção: '))
if opc == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)}.')
elif opc == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}.')
elif opc == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}.')
else:
    print(f'Não reconheço a opção {opc}')