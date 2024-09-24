menu = input("Aperte 1 para continuar")
for i in menu:
    nome = input("Digite o seu nome: ")
    if nome == nome[0:3]:
        print ("Nome precisa ter mais que 3 caracteres")
    idade = int(input("Insira a sua idade: "))
    if idade<0 or idade>150: 
        print ("Idade inválida")
    else: 
        salario = int(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Salário inválido")
        else:
            sex = print("F - Feminino\nM - Masculino")
            sexo = input("Digite o seu sexo: ")
            if sexo == "F" or sexo == "M" :
                civil = print("S - Solteiro\nC - Casado(a)\nV - Viuvo(a)\nD- Divorciado(a)")
                estado = input("Escolha uma das opções acima: ")
                if estado == "S" or estado == "C" or estado == "V" or estado == "D":
                    print("Informações confirmadas")
                    break
                else:
                    print("Estado civil inválido")
            else:
                print("Sexo inválido")