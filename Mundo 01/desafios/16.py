# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

n = float(input('Digite um numero fracionario: '))

print(f'O nuemro que vc digitou é {n} e a sua porção inteira é {int(n)}')
print(f'O nuemro que vc digitou é {n} e a sua porção inteira é {trunc(n)}')