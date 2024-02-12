# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

k = float(input('Qual a quantidade de KM percorrido?: '))
d = int(input('Quantidade de dias usando o carro?: '))

dias = d*60
km = k*0.15

print(f'O valor a pagar é: {dias+km:.2f}')