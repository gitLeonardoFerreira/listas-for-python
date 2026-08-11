def calcular_dissidio (salario:float, percentual:float = 0.08) -> float:
    if percentual >= 1 :
        percentual /= 100
    salario_aumento = salario * (1 + percentual)
    return salario_aumento


#o parametro defalt é aquele valor que é definido na funcao para quando
#nao quisermos passar o valor
salario_atual = 10000
print(f'com o dissidio o seu salario passou de R${salario_atual:.2f} para '
    f'R${calcular_dissidio(salario=salario_atual, percentual=0.5):.2f}')



def mostrar_informações(nome:str, idade:int, cidade:str):
    return print(f'{nome} - {idade} - {cidade}')

mostrar_informações('Luiz', 56, 'São Paulo')

def soma(a:float, b:float) -> float:
    soma = a + b
    return print(soma)

soma(4.5, 6)

def enviar_email(destinatario:str, assunto:str = 'sem assunto', corpo:str = '') -> str:
    print(f'{destinatario}, {assunto}, {corpo}')

enviar_email('Daniel', 'boas vindas', 'Olá dan!')