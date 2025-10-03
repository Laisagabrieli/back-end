# Exemplo básico de backend que recebe um nome e retorna saudação
def saudacao(nome):
    nome = nome.strip()
    if len(nome) == 0:
        return "Nome não pode ser vazio."
    elif len(nome) < 3:
        return "Nome muito curto!"
    else:
        return f"Olá, {nome}! Seja bem-vindo(a)!"

# Exemplo de uso
if __name__ == "__main__":
    nome_usuario = input("Digite seu nome: ")
    print(saudacao(nome_usuario))
