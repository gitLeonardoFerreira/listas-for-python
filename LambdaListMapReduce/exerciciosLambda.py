#ex 1
from functools import reduce

par_ou_impar = lambda x: f'o numero {x} é par' if x % 2 == 0 else f'o numero {x} é impar'
print(par_ou_impar(5))

#ex2
lista_precos = [100.0, 250.0, 39.90]
lista_desconto = [0.1, .2, 0.05]
print(list(map(lambda x: round(x*0.9,2), lista_precos)))

#desafio
preco = 100
desconto = 0.1
def preco_desconto(p, d):
    return p * (1 - d)

print(f'Com {desconto} de desconto meu preco {preco} sera {preco_desconto(preco, desconto)} ')

preco_descontos = list(map(preco_desconto,lista_precos,lista_desconto))
print(preco_descontos)

#usando lambda
print(list(map((lambda p,d: round(p*(1-d), 2)), lista_precos,lista_desconto)))

#ex4
lista_nome = ['ana', 'bruna', 'carla']
def para_maiuscula(str):
    return str.upper()

print(list(map(para_maiuscula,lista_nome)))

print(list(map(lambda x: x.upper(), lista_nome)))

#ex5
from functools import reduce
def multiplica(m,n):
    return m*n
numeros = [2, 3, 5, 5]
total = reduce(multiplica, numeros)
print(total)

#ex6
numero_maior = [15, 42, 8, 99, 23]
from functools import reduce
print(reduce((lambda x,y: x if x > y else y), numero_maior))