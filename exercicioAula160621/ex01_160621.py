#01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

l = [5,7,2,9,4,1,3]
#tamanho da lista
print(len(l))
#maior valor
print(f'O maior valor é: ',max(l))
#menor valor
print(f'O menor valor é: ',min(l))
#soma dos elementos
print(f'O valor da soma dos elementos é: ',sum(l))
#ordem crescente
l.sort()
print(f'Lista Crescente: {l}')
#Ordem decrescente
l.reverse()
print(f'Lista Decrescente: {l}')