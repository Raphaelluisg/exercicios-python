#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

soma_pares = 0
conta = 0

for c in range(1, 7):
    numeros = int(input('Digite o {}° número: '.format(c)))
    if numeros % 2 == 0:
        soma_pares += numeros
        conta += 1
print('A quantidade de números pares digitados é de {}, e sua soma é de {}.'.format(conta, soma_pares))
