# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('Informe um valor em metro: '))
mm = n*1000
c = n*100
dm = n*10
dam = n/10
hm = n/100
km = n/1000

print(f'{n} metros são {km} quilômetro')
print(f'{n} metros são {hm} hectômetro')
print(f'{n} metros são {dam} decâmetro')
print(f'{n} metros são {dm} decímetro')
print(f'{n} metros são {c} centímetro')
print(f'{n} metros são {mm} milímetro')