print('Revisao Map')
def dobro (n:int) -> int:
    return n * 2
numeros = [7, 87, 90, -23, 4, 0]
numeros_dobrados = list(map(dobro, numeros))
print(numeros)
print(numeros_dobrados)

print('\nRevisao Map')
def mult (n:int, m:int) -> int:
    return n * m
numeros = [7, 87, 90, -23, 4, 0]
multiplicadores = [2, 3, 4, 5, 6, 7]
multiplicados = list(map(mult, numeros, multiplicadores))
print(multiplicados)

multiplicados2 = list(map((lambda n,m: n*m), numeros, multiplicadores))
print(f'\nMultiplicados com lambda = {multiplicados2}')

print('\nList Comprehension')
#feito para simplificar o map 
#e ele retorna uma lista

#modo roots sem o list comprehension
numeros = [7, 87, 90, -23, 4, 0]
dobrados = []
for n in numeros:
    dobrados.append(n*2)

#com o list comprehension
dobrados2 = [n * 2 for n in numeros]
print(dobrados2)

print('\nCom o list comprehension e condicional')
numeros = [7, -87, 90, -23, 4, 0]
dobrados_positivos = [n * 2  if n > 0 else n**2 for n in numeros]
print(dobrados_positivos)