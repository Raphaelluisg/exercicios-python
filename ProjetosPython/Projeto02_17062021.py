# Utilizando os conceitos aprendidos até estruturas de repetição, crie um 
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de 
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha 
# de quantidade de rodadas, se não finalize o programa.
from random import randint
from time import sleep
lista = (" ", "Pedra", "Papel", "Tesoura")
comp = randint(1,3)
partidas = ' '
print('-'*41)
print('PEDRA - PAPEL - TESOURA'.center(40))
print('-'*41)
print('''\n[ 1 ] Pedra
[ 2 ] PAPEL
[ 3 ] TESOURA\n''')
print('='*30)
player = int(input('Qual é a sua opção?: '))
print('\n             JO')
sleep(1)
print('\n             KEN')
sleep(1)
print('\n             PO')
sleep(1)
print('='*30)
print('Você escolheu: {}'.format(lista[player]))
print('O computador escolheu: {}'.format(lista[comp]))
while partidas not in 'Nn':
    partidas = str(input('Deseja jogar novamente? [S/N]'))
if comp == 1: #Computador jogando Pedra
    if player == 1:
        print('EMPATE')
    elif player == 2:
        print('VOCÊ GANHOU')
    elif player == 3:
        print('VOCÊ PERDEU')
elif comp == 2: #Computador jogando Papel
    if player == 1:
        print('VOCÊ PERDEU')
    elif player == 2:
        print('EMPATE')
    elif player == 3:
        print('VOCÊ GANHOU')
elif comp == 3: #Computador jogando Tesoura
    if player == 1:
        print('VOCÊ GANHOU')
    elif player == 2:
        print('VOCÊ PERDEU')
    elif player == 3:
        print('EMPATE')

