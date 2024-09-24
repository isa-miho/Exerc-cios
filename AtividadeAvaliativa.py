tarefas = []
ordem = 0
while True:
    adc = {}
    print("=== MENU ===")
    print ("1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Marcar tarefa como concluída\n4 - Remover tarefa\n5 - Sair ")
    acao = int(input("Escolha o que fazer em seguida: "))
    if acao == 1:
        adc["Descrição"] = input("Insira a descrição da tarefa: ")
        status = int(input("Qual o status dessa tarefa?\n1 - Concluída\n2 - Não concluida\n"))
        if status == 1:
            adc["Status"] = "Concluída"
        elif status ==2:
            adc["Status"] = "Não concluída"
        adc["Ordem"] = ordem
        ordem += 1
        tarefas.append(adc)
    elif acao == 2 :
        print (f'Sua lista de tarefas:\n{tarefas}')
    elif acao == 3:
        concluir = int(input("Qual a ordem da tarefa?: "))
        for i in range(len(tarefas)):
            if i == concluir:
                tarefas[i]["Status"] = "Concluida"
                break
    elif acao == 4:
        concluir = int(input("Qual a ordem da tarefa?: "))
        for i in range(len(tarefas)):
            if i == concluir:
                tarefas.pop(concluir)
                ordem -= 1
                print("Tarefa removida com sucesso")
                break
        for i in range(len(tarefas)):
            if tarefas[i]["Ordem"] > concluir:
                tarefas[i]["Ordem"] -= 1
    elif acao == 5:
        print("Obrigado por usar o nosso sistema!\nENCERRANDO...")
        break
    