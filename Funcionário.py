class Funcionario:
    def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    def nome_completo(self): 
        print (f'Nome completo do funcionário: {self.nome} {self.sobrenome}')
    def incrementar_hora (self,extra):
        self.horas_trabalhadas += extra
    def calcular_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora
        print(f'Salário do funcionário: R${self.salario}')
funcionario1 = Funcionario("Stefanie","de Oliveira",40,5,)
funcionario1.nome_completo()
funcionario1.incrementar_hora(5)
funcionario1.calcular_salario()
funcionario2 = Funcionario("Camila","da Silva Souza",60,7)
funcionario2.nome_completo()
funcionario2.incrementar_hora(5)
funcionario2.calcular_salario()