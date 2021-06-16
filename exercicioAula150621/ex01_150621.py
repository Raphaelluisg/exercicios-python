#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesomaior = 200
pesomenor = 0
int.format(0, 200)

for c in range(1,6):
    n = int(input('Informe o peso da {}: '.format(c)))
    if n > pesomaior:
        pesomaior = n
    if n < pesomenor:
        pesomenor = n
print('O maior peso é de {}kg, e o menor é de {}kg'.format(pesomenor, pesomaior))