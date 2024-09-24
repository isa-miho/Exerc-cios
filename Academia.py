class Aluno:
    def __init__(self,nome,idade,peso,altura,mensalidade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    def desconto(self):
        if self.idade < 18 :
            self.cupom = self.mensalidade * 0.1
            print("Parabéns você recebeu 10 por cento de desconto!")
            self.mensalidade -= self.cupom
        else:
            pass
    def calcular_imc(self):
        self.imc = self.peso/ (self.altura**2)
        print(f'IMC do aluno: {self.imc}')
    def detalhes(self):
        print(f'Nome do aluno: {self.nome}')
        print(f'Idade do aluno: {self.idade}')
        print(f'Peso do aluno: {self.peso}')
        print(f'Altura do aluno: {self.altura}')
aluno1 = Aluno("Alyssa",15,48,1.54,120)
aluno1.desconto()
aluno1.calcular_imc()
aluno1.detalhes()
aluno2 = Aluno("Ryle",29,87,1.87,120)
aluno2.desconto()
aluno2.calcular_imc()
aluno2.detalhes()