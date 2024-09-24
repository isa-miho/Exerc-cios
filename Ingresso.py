class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco 
        self.setor = setor
    def alterar_preco(self):
        self.preco = float(input("Insira o novo valor do ingresso: "))
        print(f"Valor alterado com sucesso!\nNovo valor: {self.preco}")
    def mostrar_setor(self):
        print(f'Setor {self.setor}')
class Ingresso_Vip(Ingresso):
    def __init__(self, preco, setor,camarote,open_bar,open_food,estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento
        camarote = True
        open_bar = True
        open_food = True
        estacionamento = True
    def pegar_bebida(self):
        if self.open_bar:
            print("Sua bebida foi pega com sucesso!")
        else:
            print("Você não tem acesso ao open bar")
    def acessar_camarote(self):
        if self.camarote:
            print("Bem vindo ao camarote!")
        else:
            print("Você não tem acesso ao camarote")
cliente1 = Ingresso(100,"Normal")
cliente1.alterar_preco()
cliente1.mostrar_setor()
cliente2 = Ingresso_Vip(100,"Vip",True,True,True,True)
cliente2.alterar_preco()
cliente2.mostrar_setor()
cliente2.pegar_bebida()
cliente2.acessar_camarote()
cliente3 = Ingresso_Vip(100,"Normal",False,False,False,False)
cliente3.alterar_preco()
cliente3.mostrar_setor()
cliente3.pegar_bebida()
cliente3.acessar_camarote()