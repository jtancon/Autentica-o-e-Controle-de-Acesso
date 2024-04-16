import json

def autenticar_usuario(usuarios, login, senha):
    if login in usuarios and usuarios[login] == senha:
        return True
    else:
        return False

def verificar_permissao(permissoes, usuario, acao, recurso):
    if usuario in permissoes and acao in permissoes[usuario] and recurso in permissoes[usuario][acao]:
        return True
    else:
        return False

with open('usuarios.json', 'r') as usuarios_file:
    usuarios = json.load(usuarios_file)

with open('permissoes.json', 'r') as permissoes_file:
    permissoes = json.load(permissoes_file)

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if autenticar_usuario(usuarios, login, senha):
    print("Autenticação bem-sucedida. Bem-vindo,", login)
else:
    print("Usuário ou senha inválidos. Encerrando programa.")
    exit()

acao = input("Qual ação deseja realizar (ler, escrever, apagar)? ")
recurso = input("Qual arquivo deseja acessar? ")

if verificar_permissao(permissoes, login, acao, recurso):
    print("Acesso permitido.")
else:
    print("Acesso negado.")
