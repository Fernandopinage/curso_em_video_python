# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('Qual o valor do produto? R$ '))
desconto = 5
totalDesconto =  n * 5 / 100
print(f'O produto custava {n}R$, na promoção com desconto de 5% vai custar {n-totalDesconto}R$')