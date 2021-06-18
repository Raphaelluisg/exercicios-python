#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

n1 = list()
while True:
    p = int(input('Digite um número: '))
    if p not in n1:
        n1.append(p)
        print('Número adicionado.')
    else:
        print('Número duplicado')
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('\nPrograma finalizado1')
n1.sort() #Colocar em ordem crescente
print(f'Os números digitados foram {n1}')
