usuarioUM = ["usuario123","usuario_123","usuario_456"]
senhaUm = ["senha123","senha_123","senha456"]
for i in usuarioUM:
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")
    if usuario == usuarioUM[0] or usuario == usuarioUM[1] or usuario== usuarioUM[2]:
        if senha== senhaUm[0] or senha==senhaUm[1] or senha == senhaUm[2]:
            print("Acesso concedido")
            break
        else:
            print ("Usuário ou senha inválidos")
