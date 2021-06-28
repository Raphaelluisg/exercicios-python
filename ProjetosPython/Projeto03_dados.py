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

matches_play = dict() # dict para adicionar todos as rodadas
# para atribuir os jogadores para a partida

match = {input(f'\nPlayers Name {i}: ').capitalize(): randint(1,20) for i in range(1,5)}
print()
print('\nOs números sorteados foram:')
for k, v in match.items(): # key e value para poder receber o valor(número) tirado por cada jodador
    sleep(1), print(f'\nO {k} tirou {v} no dado.')
    matches_play = sorted(match.items(), key=itemgetter(1), reverse=True)# O reverse colocado para poder que os números jogado sejam do maior para o menor, colocados em ordem com o itemgetter.
    # print(matches_play)
print()
print('=='*22)
print(f'| {"RANKING":^40} |')
print('=='*22)
print(f'|  Colocação  |   Jogador   |   Resultado  |')
print('=='*22)
colocacao =1
for p in range(len(matches_play)):
    if p == 0 or matches_play[p][1] == matches_play[p-1][1]:
            print(f'|  {str(colocacao) + "°":^10} |  {matches_play[p][0]:^10} |   {matches_play[p][1]:^10} |')
    else:
            colocacao +=1
            print(f'|  {str(colocacao) + "°":^10} |  {matches_play[p][0]:^10} |   {matches_play[p][1]:^10} |')
print('=='*22)
