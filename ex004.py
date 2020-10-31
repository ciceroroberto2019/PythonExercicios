teste = input('Digite qualquer coisa para validar: ')
print('O tipo primitivo desse valor é ', type(teste))  # verifica o tipo de dado
print('Só tem espaço? ', teste.isspace())
print('É um numero? ', teste.isnumeric())
print('É alfabético? ', teste.isalpha())
print('É alfanumerico ? ', teste.isalnum())
print('Esta em maiusculo? ', teste.isupper())
print('Esta em minusculo? ', teste.islower())
print('Esta capitalizada? {}'.format(teste.istitle()))
