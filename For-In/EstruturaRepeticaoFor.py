"""
Há uma outra estrutura de repeticao que serve para
quando sabemos sabemos de antemao quantas repeticao vamos ter
FOR
--> percorrer ELEMENTOS ITERAVEIS
"""
# titulo = 'Estrtura de repetica FOR'
# print(f'{titulo:^30}')
# titulo = 'TABUADA'
# print(f'{titulo:^30}')
# #enquanto o while nó temos que controlar o contador
# #o for faz isso de maneira automatica
# #1a versao
# n = int(input('Entre com um numero inteiro para a tabuada: '))
# for numero in (1,2,3,4,5,6,7,8,9,10): #o numero aqui representa um contador
#     tabuada = n * numero
#     print(f'{n} X {numero} = {tabuada}')

"""
existe uma maneira de abreviar essa lista de numeros
é o comando RANGE
range nada mais é que um gerador de numeros de um intervlo
SINTAXE
range(inicio, fim, incremento)
no uso precisamos acrescentar no parametro de fim pois ele come um do final
range(inicio, fim, +1, incremento

range(quantidade de numeros)
lembrar que desse jeito ele coeça no zero
"""

#existe uma maneira de abreviar essa lista de numeros
#é o comando RANGE
#RANGE nada mais é que um gerador de numeros de um intervalo
#1a maneira de uso é passar a quantidade de numeros necessarios
# print('Gerando 5 numeros')
# for i in range(5):
#     print(i)
# print('\n')
# for i in range(5):
#     print(i+1)
#
# #será que o range pode gerar os numeros a partir de um numero escolhido?
# # por exemplo a partir do 1
# #2a maneira - passando o inicio e o final
# print('Gerando 5 numeros a paritr de um inicio')
# for i in range(1,6): #range é intervalo aberto [1,5[, por isso se deve acrescentar mais um (1,6)
#     print(i)
# print('\n')
# for i in range(1,5+1):
#     print(i)
#
# #existe mais um parametro no range
# #o ultimo parametro chamamos de incremento ou pulo
# print('Gerando numeros a paritr de um inicio e com pulo de 2 (até a o numero 5)')
# #desse jeito ele comeu o ultimo numero
# for i in range(5):
#     print(i)

n = int(input('Entre com um numero inteiro para a tabuada: '))
for numero in range(1,11): #o numero aqui representa um contador
    tabuada = n * numero
    print(f'{n} X {numero} = {tabuada}')

print('\n')
n = int(input('Entre com um numero inteiro para a tabuada: '))
for numero in range(1,10+1): #o numero aqui representa um contador
    tabuada = n * numero
    print(f'{n} X {numero} = {tabuada}')