frase=input('Digite uma frase: ')
print('essa frase e alphanumerica?', frase.isalnum())   #verifica se a frase tem letras e numeros
print('essa frase e alfabetica?', frase.isalpha())  #verifica se a frase tem apenas letras
print('essa frase e numerica?', frase.isdigit())  #verifica se a frase tem apenas numeros
print('essa frase e decimal?', frase.isdecimal())  #verifica se a frase tem apenas numeros decimais
print('essa frase e um identificador?', frase.isidentifier())  #verifica se a frase pode ser um identificador valido em Python
print('essa frase e imprimivel?', frase.isprintable())  #verifica se a frase pode ser impressa
print('essa frase e um espaço?', frase.isspace())  #verifica se a frase tem apenas espaços
print('essa frase e um titulo?', frase.istitle())  #verifica se a frase está em formato de título (primeira letra de cada palavra maiúscula)
print('essa frase e um digito?', frase.isdigit())  #verifica se a frase tem apenas dígitos
print('essa frase e um simbolo?', frase.isascii())  #verifica se a frase contém apenas caracteres ASCII
print('essa frase e numerica?', frase.isnumeric()) #verifica se a frase tem apenas caracteres numéricos
print('essa frase esta em maiusculas?', frase.isupper())  #verifica se a frase está em maiúsculas
print('essa frase esta em minusculas?', frase.islower()) #verifica se a frase está em minúsculas
print('essa frase esta capitalizada?', frase.istitle()) #verifica se a frase está capitalizada (primeira letra maiúscula e o restante minúsculo)
print('quantidade de caracteres:', len(frase)) #conta o número de caracteres na frase
