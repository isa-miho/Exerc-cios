from funções import Funcoes 
from agendamento import Agendamento 
def ExibirMenu():
    print("=====Bem-vindo!=====") 
    print("-----MENU-----") 
    print("1 - Agendar") 
    print("2 - Cancelar agendamento") 
    print("3 - Visualizar agendamentos") 
    print("4 - Sair") 
    print("-" * 15) 
funcao = Funcoes() 
while True: 
    ExibirMenu() 
    op = int(input("Digite a opção: ")) 
    if op == 1: 
        try:
            nome = input("Digite o nome do cliente: ") 
            data = input("Digite a data do agendamento: ") 
            hora = input("Insira o horário do agendamento: ") 
            servico = input("Digite o tipo de serviço que será realizado: ") 
            agendamento = Agendamento(nome, data, hora, servico) 
            funcao.Agendar(agendamento)
        except Exception as a:
            print (f'O erro foi: {a}')
    elif op == 2: 
        nome = input("Digite o nome do cliente: ") 
        funcao.CancelarAgendamento(nome) 
    elif op == 3: 
        funcao.MostrarAgendamentos() 
    elif op == 4: 
        print("Obrigado por usar o nosso sistema!") 
        break 
    else: 
        print("Opção não encontrada, tente novamente")