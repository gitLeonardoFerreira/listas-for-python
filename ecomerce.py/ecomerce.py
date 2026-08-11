NOME = 0
PRECO = 1
ESTOQUE = 2

loja = [['Camiseta azul', 89.90, 50], ['Tenis Runner', 449.99, 70]]



def cadastar_pruduto (catalogo:list[list[object]], nome:str, preco:float, estoque:int) -> list[list[object]]:
    """Cadastrar um produto em um catalogo
    
    params: :catalogo lista de produtos
    :nome nome do produto
    :preco preco do prduto
    :estoque quantidade de estoque

    Returns: lista de produtos cadastrados"""

    catalogo.append([nome, preco, estoque])
    return catalogo


def exibir_catalogo (catalogo:list[list[object]]) -> None:
     for produto  in catalogo:
        print(f'{produto[NOME]} - R$: {produto[PRECO]:.2f} - (estoque:{produto[ESTOQUE]})')

exibir_catalogo(loja)