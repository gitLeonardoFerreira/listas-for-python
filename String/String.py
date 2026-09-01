#String se comporta como se fosse uma lista
#Sao uma sequencia de caracteres

frase = 'Eu amo Python'
print(frase)
lista = frase.split()
print(lista)

primeira_palavra = lista[0]
print(primeira_palavra)
letra = primeira_palavra.split()
print(letra)

primeira_palavra = lista[0]
print(primeira_palavra)
letra = primeira_palavra[0]
print(letra)

frase = 'Eu amo Python'
for palavra in frase.split():
    print(palavra)

print('\nSlicing de uma string')
frase = 'Eu amo python'
lista_palavras = frase.split()
amor = lista_palavras[0:2]
print(amor)

print('\nSlicing de uma frase - dividindo em letras')
indices = '0123456789123'
frases = 'Eu amo Python'
print(frases[0:2])
print(frases[0:6])
print(frase[-1:0:-1]) #Come o E final
print(frase[::-1])
print(frase[-1:-3:-1]) #os dois ultimos caracteres

#Ex 5
tupla = (3, 15, 7, 42, 8, 19, 4, 26, 11)
print(tupla[0:4])
print(tupla[-1:-4:-1])
print(tupla[::-1])