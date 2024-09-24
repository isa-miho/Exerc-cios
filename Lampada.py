lampada = False
def ligarLampada():
    return True
def desligarLampada():
    return  False
def consultarLampada():
    if lampada:
        print("Acessa")
    else:
        print("Desligada")
while True:
    print("1 - Ligar lampada\n2 - Desligar lampada\n3 - Consultar lampada")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        lampada = ligarLampada()
    elif opcao == 2:
        lampada = desligarLampada()
    elif opcao ==3:
        lampada = consultarLampada()