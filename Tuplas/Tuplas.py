#é também uma coleção
#ela é imutavel: nasce e morre do mesmo jeito

#ela é indexada (posicional), ela é heterogenea

minhaTupla = ('sol', 'agua', 'natureza')
print(minhaTupla)

print('\nTipos de dados diferente')
outraTupla = tuple(('a', 45, True))
print(type(outraTupla))
print(outraTupla)

print('\nAcessando pela posição')
print(f'1a posicao: {minhaTupla[0]}')
print(f'2a posicao: {minhaTupla[2]}')
print(f'Ultima posicao: {minhaTupla[-1]}')

print('\nPegadinha')
#não faz sentido criar uma tupla vazia, pois nao podemos acrescentar elementos
tuplaVazia = ()

print('\nPegadinha 2')
tuplaFalse = ('sol')
print(tuplaFalse)
tuplaTrue = ('sol',)

print('\nAchando a posicao de um elemento')
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(f'A agua esta na posicao: {minhaTupla.index('agua')}')
print(f'O 1o sol esta na posicao: {minhaTupla.index('sol')}')
print(f'O proximo sol esta na posicao: {minhaTupla.index('sol', 1)}')
#podemos somar com minhaTupla.index(sol, minhaTupla.index(sol + 1) porém a partir da 3a
#posicao já nao é mais recomendado

('\nPercorrendo a colecao toda')
print(minhaTupla)
for item in minhaTupla:
    print(item)
#achando a posicao dos sois

#o enumerate traz o par (indice, item)
#e ai usamos a atribuição multipla do python para colocar nas respectivas variaveis
for indice, item in enumerate(minhaTupla):
    if item == 'sol':
        print(f'\n{indice,item}')

print('\nMatriz de tuplas')
matrizTupla = (('café', 'banho'), ('almoco', 'academia'), ('aula', 'series'))
print(matrizTupla)
print(matrizTupla[2][1])

#unpacking -atribuicao multipla
pessoa = ('Patricia', 'Casada', 54)
nome, estado_civil, idade = pessoa
print(nome)
print(estado_civil)
print(idade)

print('\nConversao para gambiarrar')
#acrescentar um elemento ???? não tem append
#como fazer
temp = list(minhaTupla)
temp.append('gambiar')
print(type(temp))
minhaTupla = tuple(temp)
print(minhaTupla)
del temp