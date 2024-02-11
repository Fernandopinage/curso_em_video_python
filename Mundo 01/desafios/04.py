# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele


algo = input('digite algo: ')

print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Só tem espaço? {algo.isspace()}')
print(f'É um numero ? {algo.isnumeric()}')
print(f'É alfabetico ? {algo.isalpha()}')
print(f'É alfanumerico ? {algo.isalnum()}')
print(f'Está maiusculas ? {algo.isupper()}')
print(f'Está em minuscula ? {algo.islower()}')
print(f'Está em capitalizada ? {algo.istitle()}')