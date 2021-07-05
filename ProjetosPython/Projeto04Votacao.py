# Projeto 04 - Simulador de votação:  

from datetime import date
from time import sleep

#função para poder fazer a tela inicial com todas as instruções para o eleitor
def telaInicial():
    sleep(1)
    print('\n#####################################')
    print('\n        ELEIÇÕES 2021')
    print('\n#####################################')
    print('Vote em seu candidato desejado...')
    print('Se o seu candidato Ze Pimenteira, aperte [1]')
    print('Se deseja votar em Leidi Dai, aperte [2]')
    print('Se deseja votar em Free William da Silva, aperte [3]')
    print('Para votar nulo, digite [4]')
    print('Para votar em branco, digite [5]')
    print('Para finalizar é [0]')
    print('\n#####################################')

#biblioteca utilizada para poder calcular a idade do eleitor.
def autorizaVoto(anoNasc):
    atual = date.today().year
    idade = atual - anoNasc
    
    if idade < 16:
        autorizacao='Voto Negado'
    elif 16>=idade<18 and idade>=70:
        autorizacao='Voto Opcional'
    else:
        autorizacao='Voto Obrigatório.'
    return autorizacao

def votacao(autorizacao, voto):
    if autorizacao=='Voto Negado':
        return'Você não pode votar'
    elif autorizacao=='Voto Obrigatório':
        voto+=1
    


                  
            
telaInicial()
input('\nDigite ENTER para começar.')
print(f'\n{"="*10} CONDIÇÃO DE VOTO{"="*10}\n')
anoNasc=int(input('Digite o ano de seu nascimento: '))
print(autorizaVoto(anoNasc))
