
class Carro:
    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 2015
    km_rodados = 0
    status_motor = "desligado"
    status_movimento = "parado"
    def detalhes(self):
        print (f'{self.cor}')
        print (f'{self.marca}')
        print (f'{self.ano}')
        print (f'{self.km_rodados}')
    def ligarMotor(self):
        self.status_motor = "ligado"
        print (f'{self.status_motor}')
    def deligarMotor(self):
        self.status_motor = "desligado"
        print (f'{self.status_motor}')
    def andar(self):
        self.status_movimento = "andando"
        print (f'{self.status_movimento}')
    def parar(self):
        self.status_movimento = "parado"
        print (f'{self.status_movimento}')
carro1 = Carro()
carro1.cor = "Prata"
carro1.marca = "Hyundai"
carro1.modelo = "HB20"
carro1.ano = 2020
carro1.km_rodados = 5
carro1.detalhes()
carro1.ligarMotor()
carro1.andar()
