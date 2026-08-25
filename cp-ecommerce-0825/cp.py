# ecommerce.py
# Projeto de fundo - E-commerce simples
# Atividade avaliativa (conteúdo até a Aula 03): login de usuário e menus
# diferenciados.
from functools import reduce
# ============================================================
# CONSTANTES
# ============================================================
# Índices de cada campo dentro da lista que representa um produto.
NOME = 0
PRECO = 1
ESTOQUE = 2
# Índices de cada campo dentro da lista que representa um usuário
# ([nome, email, senha]).
NOME_USUARIO = 0
EMAIL = 1
SENHA = 2

# ============================================================
# SISTEMA — produtos (prontas desde a Aula 03, não alterar)
# ============================================================

def cadastrar_produto(
   catalogo: list[list[object]],
   nome: str,
   preco: float,
   estoque: int = 0,
) -> list[list[object]]:
   """Cadastra um novo produto no catálogo."""
   produto: list[object] = [nome, preco, estoque]
   catalogo.append(produto)
   return catalogo

def atualizar_estoque(
   catalogo: list[list[object]],
   nome_produto: str,
   quantidade: int,
) -> list[list[object]]:
   """Atualiza a quantidade em estoque de um produto já cadastrado."""
   for produto in catalogo:
       if produto[NOME] == nome_produto:
           produto[ESTOQUE] += quantidade
           return catalogo
   print(f"Produto '{nome_produto}' não encontrado no catálogo.")
   return catalogo

def exibir_catalogo(catalogo: list[list[object]]) -> None:
   """Exibe todos os produtos cadastrados no catálogo."""
   for produto in catalogo:
       print(
           f"{produto[NOME]} - R$ {produto[PRECO]:.2f} "
           f"(estoque: {produto[ESTOQUE]})"
       )

def listar_nomes_produtos(catalogo: list[list[object]]) -> list[str]:
   """Lista os nomes de todos os produtos cadastrados no catálogo."""
   return [produto[NOME] for produto in catalogo]

def aplicar_reajuste_precos(
   catalogo: list[list[object]],
   percentual: float,
) -> list[list[object]]:
   """Aplica um reajuste percentual ao preço de todos os produtos."""
   fator = 1 + (percentual / 100)
   return [
       [produto[NOME], round(produto[PRECO] * fator, 2), produto[ESTOQUE]]
       for produto in catalogo
   ]

def calcular_valor_total_estoque(catalogo: list[list[object]]) -> float:
   """Calcula o valor total investido em estoque."""
   return reduce(
       lambda total, produto: total + produto[PRECO] * produto[ESTOQUE],
       catalogo,
       0.0,
   )

# ============================================================
# SISTEMA — produtos
# ============================================================

def listar_produtos_baixo_estoque(
   catalogo: list[list[object]],
   limite: int = 10,
) -> list[str]:
   """Lista os nomes dos produtos com estoque abaixo de um limite."""
   return [
       produto[NOME] for produto in catalogo if produto[ESTOQUE] < limite
   ]

# ============================================================
# SISTEMA — usuários
# ============================================================

def cadastrar_usuario(
   usuarios: list[list[str]],
   nome: str,
   email: str,
   senha: str,
) -> list[list[str]]:
   """Cadastra um novo usuário, se o e-mail ainda não estiver em uso."""
   if email_existe(usuarios, email):
       print("Aviso: e-mail já cadastrado.")
       return usuarios
   usuarios.append([nome, email, senha])
   return usuarios

def email_existe(usuarios: list[list[str]], email: str) -> bool:
   """Verifica se já existe um usuário cadastrado com o e-mail informado."""
   lista_email = [usuario[EMAIL] for usuario in usuarios]
   return email in lista_email

def fazer_login(
   usuarios: list[list[str]],
   email: str,
   senha: str,
) -> list[str] | None:
   """Verifica as credenciais e retorna o usuário correspondente."""
   for usuario in usuarios:
       if usuario[EMAIL] == email and usuario[SENHA] == senha:
           return usuario
   return None

# ============================================================
# MENUS
# ============================================================

def menu_cadastrar_usuario(usuarios: list[list[str]]) -> list[list[str]]:
   """Pede nome, e-mail e senha ao usuário e chama cadastrar_usuario."""
   nome = input("Nome: ")
   email = input("Email: ")
   senha = input("Senha: ")
   usuarios = cadastrar_usuario(usuarios, nome, email, senha)
   return usuarios

def menu_login(usuarios: list[list[str]]) -> list[str] | None:
   """Pede e-mail e senha, chama fazer_login e informa o resultado."""
   email = input("Email: ")
   senha = input("Senha: ")
   usuario = fazer_login(usuarios, email, senha)
   if usuario:
       print("Usuário logado com sucesso!")
   else:
       print("Email ou senha incorretos.")
   return usuario

def menu_produtos(catalogo: list[list[object]]) -> None:
   """Exibe o catálogo de produtos."""
   exibir_catalogo(catalogo)

def menu_logout() -> None:
   """Informa que o logout foi realizado com sucesso."""
   print("Logout realizado com sucesso.")

def menu_usuario_nao_logado(
   usuarios: list[list[str]],
   catalogo: list[list[object]],
) -> str | list[str] | None:
   """Menu mostrado a quem ainda não fez login."""
   escolha = int(
       input(
           "Escolha uma opção:\n"
           "1- Cadastrar usuário\n"
           "2- Fazer login\n"
           "3- Ver produtos\n"
           "4- Sair\n"
       )
   )
   if escolha == 1:
       menu_cadastrar_usuario(usuarios)
       return None
   elif escolha == 2:
       return menu_login(usuarios)
   elif escolha == 3:
       menu_produtos(catalogo)
       return None
   elif escolha == 4:
       return "SAIR"
   else:
       print("Opção inválida.")
       return None

def menu_usuario_logado(
   usuario_logado: list[str],
   catalogo: list[list[object]],
) -> str | list[str] | None:
   """Menu mostrado a quem já está logado."""
   escolha = int(
       input(
           "Escolha uma opção:\n"
           "1- Ver produtos\n"
           "2- Logout\n"
           "3- Sair\n"
       )
   )
   if escolha == 1:
       menu_produtos(catalogo)
       return usuario_logado
   elif escolha == 2:
       menu_logout()
       return None
   elif escolha == 3:
       return "SAIR"
   else:
       print("Opção inválida.")
       return usuario_logado

# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
if __name__ == "__main__":
   catalogo: list[list[object]] = []
   catalogo = cadastrar_produto(catalogo, "Camiseta Azul", 59.90, 120)
   catalogo = cadastrar_produto(catalogo, "Tênis Runner", 199.90, 60)
   catalogo = cadastrar_produto(catalogo, "Boné Preto", 39.90, 50)
   usuarios: list[list[str]] = []
   usuario_logado: list[str] | None = None
   while True:
       if usuario_logado is None:
           resultado = menu_usuario_nao_logado(usuarios, catalogo)
       else:
           resultado = menu_usuario_logado(usuario_logado, catalogo)
       if resultado == "SAIR":
           print("SAIR")
           break
       usuario_logado = resultado