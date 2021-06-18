# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogos = list()
sena = list()
print('-'*41)
print('BOLÃO DA MEGA SENA'.center(40))
print('-'*41)
sorteio = int(input('Quantos jogos deseja realizar? '))
while True:
    while len(jogos) != 6:
        numeros = randint(1, 60)
        if numeros not in jogos:
            jogos.append(numeros)
    sena.append(jogos[:])
    jogos.clear()
    if len(sena) == sorteio:
        break
for i, v in enumerate(sena):
    print(f'Jogo {i+1}: {sorted(v)}')
    sleep(1)
print('-'*41)
print('BOA SORTE!!!'.center(40))
print('-'*40)
