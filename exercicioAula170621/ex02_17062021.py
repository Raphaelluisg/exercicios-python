#02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.
n1 = list()
npares = list()
nimpares = list()
while True:
    n1.append(int(input('Digite um número: ')))
    resp = str(input('Deseja digitar um novo número? [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(n1):
    if v % 2 == 0:
        npares.append(v)
    if v % 2 ==1:
        nimpares.append(v)
print('\/'*20)
print(f'O valor da lista é: {n1}')
print(f'O valor da lista dos pares é: {npares}')
print(f'O valor da lista dos impares é: {nimpares}')
