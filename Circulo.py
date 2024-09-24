class Circulo:
    def __init__(self,raio):
        self.raio = raio
    def valor_raio(self):
        print(f'Valor do raio: {self.raio}')
    def calcular_area(self):
        self.area = 3.14 * (self.raio^2)
        print(f'Área do círculo: {self.area}')
    def calcular_circunferencia(self):
        self.circunferencia = 2 * 3.14 * self.raio
        print(f'Circunferência: {self.circunferencia}')
circulo1 = Circulo(5)
circulo1.valor_raio()
circulo1.calcular_area()
circulo1.calcular_circunferencia()
circulo2 = Circulo(7)
circulo2.valor_raio()
circulo2.calcular_area()
circulo2.calcular_circunferencia()