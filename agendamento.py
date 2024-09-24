class Agendamento: 
    def __init__(self, nome, data, hora, servico): 
        self.nome = nome 
        self.data = data 
        self.hora = hora 
        self.servico = servico 
    def __str__(self):
        return f"Nome: {self.nome}\nData: {self.data}\nHora: {self.hora}\nTipo de serviço: {self.servico}"