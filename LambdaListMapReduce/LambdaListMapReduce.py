#Lambda
#Função anonima (pequena - de uma linha só - função inLine)
#A criação da função estar proxima do uso dela
#Versateis
#Cuidado que temos que ter, é NÃO TENTAR RESOLVER TUDO COM LAMBDA
#Se voce fizer isso o seu programa fica ilegivel
from functools import reduce

from FunçõesPython.ParametroDefault import soma


#Numa função tradicional fariamos
def dobro(n:int) -> int:
    return n * 2

def dobro (n:int) -> int:
    """
    Calcula o dobr de um numero inteiro

    :param n: numero inteiro
    :return: dobro de um numero inteiro
    """

    return n * 2

print(dobro(4))

#transformar em lambda
#sintaxe lambda <argumentos/parametros> : return
#lambda SEMPRE tem um return
ldobro = lambda n : n * 2 # : equivale ao return do def
print(ldobro(79))
#o uso mais comum
print((lambda n : n * 2)(65))

#lambda CONDICIONAL
#tem um if embutido

#funcao que decide qual o maior de 2 numeros
def maior(x:int, y:int) ->int:
    if x > y:
        return x
    else:
        return y

print(maior(5, 7)) #<= parametros nomeados

#transformando em lambda
#nao é o uso mais comum
lmaior = lambda x,y: x if x > y else y # a resposta sempre esta nas pontas ( verdadeiro if ... else falso )

#uso mais comum
print((lambda x,y: x if x > y else y)(6, 8))

#posso usar o print dentro do lambda
#pode, mas cuidado
lmenor = lambda x,y: print(x) if x < y else print(y)
lmenor (8, 67) # funciona só em jupter notbook

# a melhor solução
lmenor2 = lambda x,y: f'o numero maior é {x}' if x > y else f'o numero maior é {y}'
print(lmenor2(7, 90))

#Map é ima funcionalidade do python que permite aplicar
#uma funcao  em todos os elementos de uma colecao
def dobro(n:int) -> int:
    return n * 2
numeros = [7, 87, 90, -23, 4, 0]

#da maneira roots
dobrados = []

for n in numeros:
    dobrados.append(dobro(n))
print(numeros)
print(dobrados)


print('\nCom o map')
#com o map
#sintaxe map(funcao, iteravel/colecao)
dobrados2 = list(map(dobro, numeros))
print(list(map(dobro, numeros)))
print(dobrados2)


print('\n')
#ultilizando esta funcao
nova_lista = map(lambda n: n*2, [2, 4, 6 , 8])
print(list(nova_lista))
print(list(map(lambda n: n*2, [8, 10, 20])))

#Reduce
from functools import reduce
numeros = [7, 87, 90, -23, 4, 0]
total = reduce(lambda x,y: x+y, numeros)
print(total)
