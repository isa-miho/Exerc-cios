class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade,nota1,nota2,nota3,media,faltas):
        super().__init__(matricula, nome, idade)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = media
        self.faltas = faltas
    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3)/3
    def detalhes(self):
        print(f'Matrícula do aluno: {self.matricula}')
        print(f'Nome do aluno: {self.nome}')
        print(f'Idade do aluno: {self.idade}')
        print(f'Notas do aluno: {self.nota1}, {self.nota2} e {self.nota3}')
        print(f'Média do aluno: {self.media}')
        print(f'Faltas do aluno: {self.faltas}')
    def estudar(self):
        print(f'Aluno {self.nome}, está estudando')
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,formacao,disciplina,carga_horaria,salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario
    def detalhes(self):
        print(f'Matricula do professor: {self.matricula}')
        print(f'Nome do professor: {self.nome}')
        print(f'Idade do professor: {self.idade}')
        print(f'Formação do professor: {self.formacao}')
        print(f'Disciplina do professor: {self.disciplina}')
        print(f'Carga horária do professor: {self.carga_horaria}')
        print(f'Salário do professor: {self.salario}')
    def lecionar(self):
        print(f'Professor {self.nome}, está lecionando')
aluno1 = Aluno(2024143642,"Armenio",14,7,8,7,0,4)
aluno1.calcular_media()
aluno1.detalhes()
aluno1.estudar()
prof = Professor(20171048462,"Claudio",55,"Biologia","Ciências",40,2200)
prof.detalhes()
prof.lecionar()

        