# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input("Cateto oposto: \n"))
ca = float(input("Cateto adjacente: \n"))
hi = hypot(co, ca)

print(f"A hi dos números {co} e {ca} é {hi:.2f}.")