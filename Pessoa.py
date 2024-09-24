class Pessoa:
    nome = "sem nome"
    idade = 0
    endereço = "sem endereço"
    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereço: {self.endereço}')
    def alterar_idade(self):
        self.idade = int(input("Insira a sua idade: "))
pessoa1 = Pessoa()
pessoa1.nome = "Lara"
pessoa1.alterar_idade()
pessoa1.endereço = "Rua do Limeiro"
pessoa1.detalhes()

pessoa2 = Pessoa()
pessoa2.nome = input("Digite o seu nome: ")
pessoa2.alterar_idade()
pessoa2.endereço = input("Digite o seu endereço: ")
pessoa2.detalhes()

