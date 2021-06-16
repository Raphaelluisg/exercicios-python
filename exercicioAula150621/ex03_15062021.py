#03 -  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

anoatual = 2021
maior = menor = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if anoatual - ano > 18:
        maior +=1
    if anoatual - ano < 18:
        menor += 1
print(f'{maior} atingiram a maioridade, {menor} não atingiram a maioridade')