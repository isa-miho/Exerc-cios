data = input("Digite a sua data de nascimento no formato (dd/mm/aaaa): ")
dia, mes, ano = int(data[0:2]), int(data[3:5]), int(data[6:]) 
if data[2] == "/" and data[5] == "/":
    if dia > 31 or dia < 1:
        print ("Data inválida")
    elif mes > 12 or mes < 1: 
        print ("Data inválida")
    elif mes == 2 and dia > 28:
        print ("Data inválida")
    elif mes in [4, 6, 9, 11] and dia > 30:
        print ("Data inválida")    
    elif ano > 9999 or ano < 0: 
        print ("Data inválida")
    else:
        print (f'Data {dia}/{mes}/{ano} é válida')
else:
    print("Formato de data inválido. Por favor, use o formato (dd/mm/aaaa)")