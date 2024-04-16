import json

def carregar_usuarios():
    with open('usuarios.json') as f:
        return json.load(f)

def carregar_permissoes():
    with open('permissoes.json') as f:
        return json.load(f)

def autenticar_usuario(usuarios, username, password):
    if username in usuarios and usuarios[username] == password:
        return True
    else:
        return False

def verificar_permissao(permissoes, username, acao, recurso):
    if username in permissoes:
        if acao in permissoes[username] and recurso in permissoes[username][acao]:
            return True
    return False

def main():
    usuarios = carregar_usuarios()
    permissoes = carregar_permissoes()

    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    if autenticar_usuario(usuarios, username, password):
        print("Autenticação bem-sucedida!")
    else:
        print("Usuário ou senha inválidos.")
        return

    acao = input("Digite a ação desejada (ler, escrever, apagar): ")
    recurso = input("Digite o nome do recurso: ")

    if verificar_permissao(permissoes, username, acao, recurso):
        print("Acesso permitido.")
    else:
        print("Acesso negado.")

if __name__ == "__main__":
    main()
