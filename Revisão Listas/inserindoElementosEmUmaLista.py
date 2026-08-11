titulo = 'Cadastr de uma lista'
print(f'{titulo:^30}')

#lista vazia
numeros = []
#cadastro com while True /  break
while True:
    n = int(input('Entre com um numero ou zero para sair: '))
    if n == 0:
        break
    numeros.append(n)
print(numeros)
#imprimir a colecao com elementos lado a lado
#ex: 8, 4, 6, 7,
for item in numeros:
    print(item, end=', ')