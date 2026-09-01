#Ex 1
notas = (7.5, 8.0, 6.5, 9.0)
print(notas[0])
print(notas[-1])

#Ex 2
numeros = (12, 45, 7, 23, 9, 31)
total = 0 # não se deve criar varieaveis dentro do for
for numero in numeros:
    total += numero

print(total)

#Ex 3
def contar_pares(numeros) -> int:
    pares = [n for n in numeros if n % 2 ==0 ]
    print(pares)

contar_pares(numeros)

#Ex 4
produtos_loja1 = ('Caneta', 'Caderno', 'Mochila')
produtos_loja2 = ('Estojo', 'Régua')

total_produtos = (produtos_loja1 + produtos_loja2)
print(total_produtos)

#Ex 5

#Ex 6
def menor_maior(numeros: tuple) -> tuple:
    maior = max(numeros)
    menor = min(numeros)
    return (maior, menor)
print(f'maior menor: {menor_maior((3, 15, 7, 42, 8, 19, 4, 26, 11))}')

#Ex 7
lista_nome = ['Ana', 'Bruno', 'Carla']
lista_nome = tuple(lista_nome)
print(lista_nome)

#Ex 8
notas2 = ((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0))
indice_aluno = int(input('Insira o indice do aluno: '))
media = round(sum(notas2[indice_aluno])/len(notas2[indice_aluno]), 1)
print(media)


