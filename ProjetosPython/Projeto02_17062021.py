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
jogosn = list()
partidas = 0
jogar_novamente = 'Ss'
print('-'*41)
print('PEDRA - PAPEL - TESOURA'.center(40))
print('-'*41)
print('''\n[ 1 ] Pedra
[ 2 ] PAPEL
[ 3 ] TESOURA\n''')
print('='*30)
comp = randint(1,3)
player = int(input('\nQual é a sua opção?: '))
print('Você escolheu: {}'.format(lista[player]))
print('O computador escolheu: {}'.format(lista[comp]))
print('\n             JO')
sleep(1)
print('\n             KEN')
sleep(1)
print('\n             PO!!')
sleep(0.5)
print('='*30)
while jogar_novamente == 'Ss':
    resultado = vitoriac = vitoriap = contagemvc = contagemvp = 0
    partidas = int(input('Quantos jogos deseja realizar? '))
    for i, v in enumerate(jogosn):
        print(f'Jogo {i+1}: {sorted(v)}')
        sleep(0.5)
    while partidas > resultado:
        resultado +=1
        print(f' Partida {resultado}')
        if comp == 1: #Computador jogando Pedra
            if player == 1:
                print('EMPATE')
            elif player == 2:
                print('VOCÊ GANHOU')
                vitoriap +=1
            elif player == 3:
                print('VOCÊ PERDEU')
                vitoriac +=1
        elif comp == 2: #Computador jogando Papel
            if player == 1:
                print('VOCÊ PERDEU')
                vitoriac +=1
            elif player == 2:
                print('EMPATE')
            elif player == 3:
                print('VOCÊ GANHOU')
                vitoriap +=1
        elif comp == 3: #Computador jogando Tesoura
            if player == 1:
                print('VOCÊ GANHOU')
                vitoriap +=1
            elif player == 2:
                print('VOCÊ PERDEU')
                vitoriac +=1
            elif player == 3:
                print('EMPATE')
        else:
            print("Jogada Inválida.")
            partidas +=1
    jogar_novamente = input('Deseja continuar? [S/N]: ')
    if jogar_novamente == "Ss":
            continue
    else:
            print(f'\nFIM DE JOGO.\n\n Foram {vitoriap} vitória(s) suas contra {vitoriac} contra o computador.')
            break
    if contagemvp > contagemvc:
        print(f'Você ganhou, com um total de {contagemvp} vitórias.')
    else:
        print(f'O computador ganhou com {contagemvc} vitórias.')
