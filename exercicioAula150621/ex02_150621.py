#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.
from time import sleep
n1 = int(input('Digite a tabuada desejada: '))

for c in range(1, 11):
  print(f'{n1} x {c} = {n1 * c}')
  sleep(1)