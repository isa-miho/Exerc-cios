class Funcoes: 
    def __init__(self): 
        self.agendamentos = [] 
    def Agendar(self, agendamento): 
        self.agendamentos.append(agendamento) 
    def CancelarAgendamento(self, nome): 
        encontrado = False 
        for agendamento in self.agendamentos: 
            if agendamento.nome == nome: 
                self.agendamentos.remove(agendamento) 
                print("Agendamento cancelado com sucesso")
                encontrado = True 
                break 
        if not encontrado: 
            print("Agendamento não encontrado") 
    def MostrarAgendamentos(self): 
        if not self.agendamentos: 
            print("Nenhum agendamento encontrado.") 
        else: 
            for agendamento in self.agendamentos: 
                print('-----' * 10) 
                print(agendamento) 
                print('-----' * 10) 