class Triangulo:
    def __init__(self):
        self.ladoA = int(input("Digite o valor do ladoA: "))
        self.ladoB = int(input("Digite o valor do ladoB: "))
        self.ladoc = int(input("Digite o valor do ladoC: "))
    def calcular_perimetro(self):
        self.perimetro = self.ladoA + self.ladoB + self.ladoc
        print(f'O perimetro do triangulo é: {self.perimetro}')
    def maior_lado(self):
        self.maior = max(self.ladoA,self.ladoB,self.ladoc)
        print(f'O maior lado do triangulo é {self.maior}')
triangulo1 = Triangulo()
triangulo1.calcular_perimetro()
triangulo1.maior_lado()