# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

idade = int(input('Digite sua idade: '))
opcao = " "

while opcao != sexo:
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()
    if opcao == sexo:
        print('Deseja continuar?')
    else:
        print('Informe uma opção válida.')
print('Programa finalizado')
