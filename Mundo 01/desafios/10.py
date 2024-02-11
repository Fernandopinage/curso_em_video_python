# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 3.27 = US$ 1

n = float(input('Quanto dinheiro você tem? \nR$'))

d = 4.95 # Faz o L
print(f'com {n}R$ você pode comprar US$ {n/d:.2f}.')