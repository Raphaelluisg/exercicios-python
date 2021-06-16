#  Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
opcao = 0

while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('Sua soma é de: {}'.format(n1+n2))
    elif opcao == 2:
        print('Sua multiplicação é de: {}'.format(n1*n2))
    elif opcao ==3:
        if n1>n2:
            print('O maior n° é: {}'.format(n1))
        else:
            print('O maior n° é: {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite um novo número: '))
    else:
        print('Digite uma Opção válida')
print('Operação finalizada')
