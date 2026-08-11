#Funções: outros temas
#Parametros nomeados e posicionais

def caulcular_media (python:float, webdev:float, frontend:float) -> float:
    """
    Calcula a media de python, webdev, frontend
    :param python: nota de python
    :param webdev: nota de webdev
    :param frontend: nota de frontend
    """

    return (python + webdev + frontend) / 3

media = caulcular_media(9, 8, 9.5)

#parametros nomeados
media = caulcular_media(webdev=9, frontennd=8, python=9.5)
