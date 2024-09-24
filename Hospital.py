paciente = []
escolha = 0
ordem = 0
while escolha != 3:
    consultas = {}
    print ("1 - Paciente\n2 - Médico\n3 - Sair")
    escolha = int(input("Escolha o que deseja fazer: "))
    if escolha == 1:
        consultas["Senha"] = ordem
        consultas["Nome do paciente"]= input("Digite o seu nome: ")
        consultas["CPF do paciente"] = input("Digite o seu CPF: ")
        consultas["Idade do paciente"] = int(input("Digite a sua idade: "))
        consultas["Horario da consulta"] = input("Digite o horário da consulta: ")
        paciente.append(consultas)
        ordem += 1 
        continuar = int(input("Deseja ver seu histórico de consultas? Aperte 1 para sim ou aperte 2 para sair"))
        if continuar == 1:
            print(consultas)
        elif continuar == 2:
            print("Obrigado por usar o nosso sistema!")
    elif escolha == 2:
        for op in paciente:
            print("1 - Ver lista de paciente\n2 - Realizar consulta\n3 - Liberar paciente")
            acao = int(input("Escolha o que deseja fazer: "))
            if acao == 1:
                print (op)
            if acao == 2:
                consulta = input("Digite o nome do paciente: ")
                alta = int(input("Esse paciente receberá alta? (1 - Para sim e 2 - para não): "))
                if alta == 1:
                    nome = int(input("Qual a senha do paciente?: "))
                    paciente.pop(nome)
                    ordem -= 1 
                    print("Paciente liberado com sucesso")
                elif alta == 2:
                    print("Obrigado por utilizar o nosso sistema!")
            elif acao == 3:
                nome = int(input("Qual a senha do paciente?: "))
                paciente.pop(nome)
                ordem -= 1
                print("Paciente liberado com sucesso")
                while True:
                    outro = int(input("Deseja liberar outro paciente? (1 - Para sim e 2 - para não):"))
                    if outro == 1: 
                        nome = int(input("Qual a senha do paciente?: "))
                        paciente.pop(0)
                        ordem -= 1
                        print("Paciente liberado com sucesso")
                    elif outro == 2:
                        print("Obrigado por utilizar o nosso sistema!")
                        break
    elif escolha == 3:
        print ("Obrigado por utilizar o nosso sistema!")
        break