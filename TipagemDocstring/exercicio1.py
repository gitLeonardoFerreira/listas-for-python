#Criar uma função criar_aluno com parametros nome e idade E retorna uma lista

def criar_aluno(nome: str, idade: int) -> list[object]:
    return [nome, idade]

print(f'\n{criar_aluno('Léo', 18)}')

#1
titulo: str = 'Pequeno Principe'
paginas: int = 348
preco: float = 123.89

print(titulo)
print(paginas)
print(preco)

#2

def dobrar(numero: int) -> int:
    """
    Recebe um número e retorna o dobro dele
    """
    return numero * 2

print(f'\nQual o dobro de 8?: {dobrar(8)}')

#3

def calcular_media(notas: list[float]) -> float:
    total = 0.0
    for nota in notas:
        total += nota
    media = total / len(notas)
    return round(media, 2)

print(f'\nA média de todas as notas é: {calcular_media([6, 10, 7.5])}')