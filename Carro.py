class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel,consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo
    def abastecer(self):
        self.consumo = int(input("Insira quantos litros foram usados: "))
    def andar(self):
        self.distancia = int(input("Insira quantos km foram andados: "))
    def verificar_nivel(self):
        self.nivel = self.distancia / self.consumo
    def calcular_imposto(self):
        self.imposto = self.valor * 0.025
    def detalhes(self):
        print(f"Modelo do carro: {self.modelo}")
        print(f"Marca do carro: {self.marca}")
        print(f"Cor do carro: {self.cor}")
        print(f"Ano do carro: {self.ano}")
        print(f"Valor do carro: {self.valor}")
        print(f"Nivel do carro: {self.nivel}")
        print(f"Valor do imposto: {self.imposto}")
carro1 = Carro("Versa","Nissan","Prata",2010,70500,0,0)
carro1.abastecer()
carro1.andar()
carro1.verificar_nivel()
carro1.calcular_imposto()
carro1.detalhes()