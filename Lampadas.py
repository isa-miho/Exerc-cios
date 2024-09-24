def info():
    print("Cômodo 0 = 12 watts\nCômodo 1 = 15 watts\nCômodo 2 = 18 watts\nCômodo 3 = 20 watts\nCômodo 4 = 22 watts ")
    tipo = int(input("Qual o tipo de cômodo?: "))
    return tipo
def tamanho(lar,com):
    lar = float(input("Informe a largura do cômodo: "))
    com = float(input("Informe o comprimento do cômodo: "))
    area = lar * com
    return area
def calculo(tipo,area):
    potencia = area * tipo
    lampadas = potencia/60
    return lampadas
tipo = 0
largura = 0
comprimento = 0
lampadas = 0 
area = largura * comprimento
while tipo != -1:
    tipo = info()
    area = tamanho(largura,comprimento)
    if tipo == 0:
        lampadas = calculo(12,area)
        print(f'Número de lampadas necessárias: {lampadas}')
    elif tipo == 1: 
        lampadas = calculo(15,area)
        print(f'Número de lampadas necessárias: {lampadas}')
    elif tipo == 2:
        lampadas = calculo(18,area)
        print(f'Número de lampadas necessárias: {lampadas}')
    elif tipo == 3:
        lampadas = calculo(20,area)
        print(f'Número de lampadas necessárias: {lampadas}')
    elif tipo == 4:
        lampadas = calculo(22,area)
        print(f'Número de lampadas necessárias: {lampadas}')
    elif tipo == -1:
        print("Obrigado por usar o nosso sistema\nENCERRANDO O SISTEMA")