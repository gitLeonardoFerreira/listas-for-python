#COLECOES
#são variaveis de memoria que tem multiplos valores
#cada valor é chamado de item (ou elemento) que podem ser do mesmo tipo de dado
#TODA coleção é um elemento ITERAVEL
#significa que podem ir de um em um que é percorrivel
#há varios tipos de coleções: LISTAS, CONJUNTOS(SET),
# TUPLAS, DICIONARIOS(formulario, chave/valor)

""""
Lista
caracteristicas
mais poderosa, porque é flexivel. perfomatica, conjunt de ocmandos para manipulação completos
MUTAVEL: depois de cirada, a lista permite acrescentar, retirar, modificar elementos
EXPANSÍVEL: pode aumentar seu conjunto de ddos a partir de outra lista
ACEITA TIPO DIFERENTES DE DADOS
INDEXADA: cada elemento tem uma POSIÇÃO dentro da LISTA
PERMITE DUPLICADOS
ORDENAVEIS --> a ordenacao natural so acontece se todos elementos forem do mesmo tipo
SIMBOLO: []
"""


titulo = 'Listas'
print(f'{titulo:^30}')
minhaLista=['café', 'água', 'açucar']
print(minhaLista)

#E se eu quisesse imprimir somente o café?
#Entender como acessar cada elemento pelo indice
#TODA COLECAO INDEXADA COMECA NO ZERO
minhaLista=['café', 'água', 'açucar','canela','café']
print(minhaLista)
#0          1       2       3       4
#-5        -4       -3       -2      -1
##'café', 'água', 'açucar','canela','café'
print(f'primeiro elemento:{minhaLista[0]}')#colchete acessa o indice do elemento
print(f'primeiro elemento:{minhaLista[-5]}')
print(f'segundo elemento:{minhaLista[1]}')
print(f'tamanho da lista:{len(minhaLista)}')#len = tamanho
print(f'ultimo elemento:{minhaLista[4]}')
print(f'ultimo elemento:{minhaLista[len(minhaLista)-1]}')
print(f'ultimo elemento:{minhaLista[-1]}')

#tentando acessar um indice que não existe
#print(f'ultimo elemento:{minhaLista[5]}')

#como acrescentar itens numa lista?
#O metodo append faz isso e ACRESCENTA NO FINAL
print('\n')
print(minhaLista)
minhaLista.append('chantilly')
minhaLista.append('especiarias')
print(minhaLista)

#e para remover intens da lista
#usamos o metodo pop
#ele sem parametro remove DO FIM DA LISTA
minhaLista.pop()
print(minhaLista)
minhaLista.pop()
print(minhaLista)
#MAS EU POSSO REMOVER UM ITEM ESPECIFICO COM O POP
#BASTA PASSAR O INDICE
#removendo o açucar
minhaLista.pop(2)
print(minhaLista)

#TODO ELEMENTO INTERAVEL podemos percorrer através do FOR
##for item in minhaLista:
   #print(item)
 #print('\n')
#percorrendo a lsta pelos INDICES da lista
#for i in range(len(minhaLista)):
   # print(minhaLista[i])