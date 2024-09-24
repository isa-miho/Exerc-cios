class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
    def depositar(self,dinheiro):
        self.saldo += dinheiro
        print(f'Saldo atual: {self.saldo}')
    def sacar(self,retirar):
        if self.saldo <= 0 or self.saldo < retirar :
            print("Saldo inssuficiente para realizar esta ação")
        else:
            self.saldo -= retirar
            print("Dinheiro retirado com sucesso")
            print(f'Saldo atual: {self.saldo}')
    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Número da conta: {self.numero}')
        print(f'Saldo: R${self.saldo}')
cliente0 = Conta("Alina",78912345689,458612,54.78)
cliente0.detalhes()
cliente0.depositar(46.22)

cliente1 = Conta("Evilin",45897812378,789426,73.41)
cliente1.detalhes()
cliente1.sacar(33.26)