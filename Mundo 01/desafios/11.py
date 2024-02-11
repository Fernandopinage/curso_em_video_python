# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²


largura = float(input('informe a largura da parede: '))
altura = float(input('informe a altura da parede: '))

area = largura*altura
litro = (largura * altura)/2

print(f"Sua parede tem a dimensão {largura}x{altura} e sua área é de {area}m².")
print(f"Para pintar essa parede, você precisará de {litro}L de tinta.")