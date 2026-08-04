#Python tem tipagem dinamica

x = 10
print(type(x))
nome = 'Paulo'
print(type(nome))

#Type Hints ajuda a definir o tipo de dado esperado pela variavel
#mas é apenas uma AJUDA, ou seja o python não impede que seja atribuido
#um valor com outro tipo de dados

nome: str = 'Paulo' # os : significa que a partir de agora o tipo de dado esperado é uma str
print(type(nome))

nome = 123
print(type(nome))

preco: float

preco = 7.8
print(type(preco))

#Todos os tipos de dados são aceitos no type hints
#int, float, bool, str, list, etc
disponivel: bool = True
print(type(disponivel))

#O tipo de uso mais importante é quando definimos funcoes
#Quando definimos o tipo de dado esperado como parametro e tambem o tipo
#de dados de retorno da função, estamos definindo a 
# ASSINATURA da função
# isso é importante para disponibilizarmos essas funções, ex: como API
def calcular_total(preco: float, quantidade:int) -> float:
    return preco * quantidade

print(calcular_total(preco, 2))
print(calcular_total(preco, 3))

# e quando a fuunção nao tem retorno?
def exibir_produto(produto: str, preco: float) -> None:
    print(f"{produto} - {preco}")

exibir_produto('Leite', 8.9)

#revisao de list
#--> tipo de dados composto
minhaLista:list = ['cafe','chantilly', 'biscoito']
print(minhaLista)

dadosPessoais = ['Patricia', 54, 'feminino', 'superior']
print(dadosPessoais)
print(f'Nome: {dadosPessoais[0]}')
print(f'Nome: {dadosPessoais[1]}')
dadosPessoais.append('Professora')

for item in dadosPessoais:
    print(item)



#mas e o tipo lis???
#vamos aplicar a lista usando type hint em funcoes
def somar_precos(precos: list) -> float:
    total: float = 0
    #fale que o total é um float sem falar que é u float
    #total = 0.0
    for preco in precos:
        total += preco
    return total
print('\nSomando Precos')
print(f'total: {somar_precos([10, 20, 30])}')

def criar_produto(produto: str, preco: float, quantidade: int) -> list:
    return [produto, preco, quantidade]
print('\nCriar Estoque')
print(f'Estoque: {criar_produto('Leite', 8.9, 10)}')

#tipos de dados generico: object
#quando usar -> na assinatura da funcao
#entendimento
#aqui estou criando uma lista que só aceita inteiros
idades: list[int] = [17, 54, 23]
print(f'Idades: {idades}')

#mas se eu quisesse uma lista mista
produto = ['camisa', 29.9, 8]
print(f'Produto: {produto}')
#eu poderia lançar mão do objeto generico OBJECT
produto: list[object] = ['camisa', 29.9, 8]


#DOCSTRING

def calcular_total(preco: float, quantidade: int) -> float:
    """Calcula a quantidade total de um produto

    Args:
        :param preco: preco unitario do produto
        :param quantidade: quantidade total de um produto

    Returns:
        total: preco total (preco * quantidade)
    
    """
    return preco * quantidade