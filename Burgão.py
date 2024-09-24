comida = int(input("Digite o código do sanduíche desejado: "))
bebida = int(input("Digite o código da bebida desejada: "))
if (comida> 103 or comida<100) and (bebida>203 or bebida<201):
    print("Código inválido")
cachorroqnt = 100
ovo = 101
bauru = 102
hamburguer = 103
refri = 201
suco = 202
agua = 203
if comida == 100 and bebida == 201:
    print ("Valor total de R$17.20")
if comida == 100 and bebida == 202:
    print("Total de R$18.70")
if comida == 100 and bebida == 203:
    print ("Total de R$15.90")
if comida == 101 and bebida == 201:
    print ("Valor total de R$14.30")
if comida == 101 and bebida == 202:
    print("Total de R$15.80")
if comida == 101 and bebida == 203:
    print ("Total de R$13.00")
if comida == 102 and bebida == 201:
    print ("Valor total de R$17.50")
if comida == 102 and bebida == 202:
    print("Total de R$19.00")
if comida == 102 and bebida == 203:
    print ("Total de R$16.20")
if comida == 103 and bebida == 201:
    print ("Valor total de R$22.20")
if comida == 103 and bebida == 202:
    print("Total de R$23.70")
if comida == 103 and bebida == 203:
    print ("Total de R$21.20")