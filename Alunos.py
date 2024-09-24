class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    def media_de_notas(self):
        self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota4)/4
    def mostrar_situacao(self):
        if self.media >= 7:
            print ("Aluno aprovado")
        elif self.media >= 5:
            print("Aluno de exame")
        elif self.media>= 0:
            print("Aluno reprovado")
    def mostrar_detelhes(self):
        print(f'Nome do aluno:{self.nome}')
        print(f'RA do aluno:{self.ra}')
        print(f'Primeira nota: {self.nota1}')
        print(f'Segunda nota: {self.nota2}')
        print(f'Terceira nota: {self.nota3}')
        print(f'Quarta nota: {self.nota4}')
aluno1 = Aluno("Jonas",2024104497,7,9,7,5)
aluno1.media_de_notas()
aluno1.mostrar_situacao()
aluno1.mostrar_detelhes()
aluno2 = Aluno("Amelia",2022304497,4,6,4,5)
aluno2.media_de_notas()
aluno2.mostrar_situacao()
aluno2.mostrar_detelhes()