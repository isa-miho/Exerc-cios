class Agenda:
    def __init__(self,dia,mes,ano,anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
    def validar_data(self):
        if self.dia > 31 or self.dia < 1:
            print ("Data inválida")
        elif self.mes > 12 or self.mes < 1: 
            print ("Data inválida")
        elif self.mes == 2 and self.dia > 28:
            print ("Data inválida")
        elif self.mes in [4, 6, 9, 11] and self.dia > 30:
            print ("Data inválida")    
        elif self.ano > 9999 or self.ano < 0: 
            print ("Data inválida")
        else:
            print (f'Data {self.dia}/{self.mes}/{self.ano} é válida')
    def anotar_tarefa(self):
        self.anotacao = input("Anote a sua tarefa: ")
    def mostrar_tarefa(self):
        print(f'Anotação da data {self.dia}/{self.mes}/{self.ano}:\n{self.anotacao}')
agenda0 = Agenda(15,8,2020,"")
agenda0.validar_data()
agenda0.anotar_tarefa()
agenda0.mostrar_tarefa()
agenda1 = Agenda(9,7,2024,"")
agenda1.validar_data()
agenda1.anotar_tarefa()
agenda1.mostrar_tarefa()