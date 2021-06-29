# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 
# jogadores joguem um dado e tenham resultados aleatórios. O programa tem que:
# • Perguntar quantas rodadas você quer fazer; 
# • Guardar os resultados dos dados em um dicionário. 
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número 
# no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande 
# campeão.

from random import randint
from time import sleep
from operator import itemgetter
rodadas= int(input('Quantas rodadas quer fazer: '))
valoresdados = [randint(1,6), randint(1,6), randint(1,6),randint(1,6)]
match = {}
for i in range(1, 5):
    match [i]= valoresdados[i-1]

vitorias= [0, 0, 0, 0]
for i in range(rodadas):
   
    print()
    print('\nOs números sorteados foram:')
    for k, v in match.items(): # key e value para poder receber o valor(número) tirado por cada jodador
        sleep(1), print(f'\nO {k} tirou {v} no dado.')
        
    matches_play = sorted(match.items(), key=itemgetter(1), reverse=True)# O reverse foi colocado para poder que os números jogado sejam do maior para o menor, colocados em ordem com o itemgetter.
    
    print('=='*22)
    for i, v in matches_play:
        if v == max(valoresdados):
            vitorias[i-1] += 1
            print(f'O jogador {i} tirou {v}. Ele pontuou!')
        else:
            print(f'O jogador {i} tirou {v}.')
    print('=='*22)
    vencedores=[]
    for i, v in enumerate(vitorias):
        if v == max(vitorias):
            vencedores.append(i+1)
if len(vencedores)==1:
    print(f'O vencedor foi jogador {vencedores[0]}')
elif len(vencedores)==2:
    print(f'Os vencedores foram os jogadores {vencedores[0]} e {vencedores[1]}')
elif len(vencedores)==3:
    print(f'Os vencedores foram os jogadores {vencedores[0]}, {vencedores[1]} e {vencedores[2]}')
else:
    print('Os 4 jogadores empataram.')

print()
print('=='*22)
print(f'| {"RANKING":^40} |')
print('=='*22)
print(f'|  Colocação  |   Jogador   |   Resultado  |')
print('=='*22)
colocacao =1
for p in range(vencedores):
    if p == 0 or vencedores[p][1] == vencedores[p-1][1]:
            print(f'|  {str(colocacao) + "°":^10} |  {match[p][0]:^10} |   {vencedores[p][1]:^10} |')
    else:
            colocacao +=1
            print(f'|  {str(colocacao) + "°":^10} |  {match[p][0]:^10} |   {vencedores[p][1]:^10} |')
print('=='*22)