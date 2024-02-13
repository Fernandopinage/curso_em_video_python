# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo de uma circunferência (ou seja, entre 0º e 360º): "))
print(f'O Angulo de {ang} tem o SENO de: {sin(radians(ang)):.2f}')
print(f'O Angulo de {ang} tem o COSSENO de: {cos(radians(ang)):.2f}')
print(f'O Angulo de {ang} tem o TANGENTE de: {tan(radians(ang)):.2f}')

