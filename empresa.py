# dados = {"nome1": "","funcao1":"","salario1":0,
#         "nome2": "", "funcao2": "", "salario2": 0,
#         "nome3":"", "funcao3": "", "salario3": 0,
#         "nome4":"", "funcao4": "", "salario4":0}
# dados ["nome1"] = input("Insira o seu nome: ")
# dados ["funcao1"] = input("Insira a sua função: ")
# dados["salario1"] = float(input("Digite o seu salário: "))
# print ("_"*30)
# dados ["nome2"] = input("Insira o seu nome: ")
# dados ["funcao2"] = input("Insira a sua função: ")
# dados["salario2"] = float(input("Digite o seu salário: "))
# print ("_"*30)
# dados ["nome3"] = input("Insira o seu nome: ")
# dados ["funcao3"] = input("Insira a sua função: ")
# dados["salario3"] = float(input("Digite o seu salário: "))
# print ("_"*30)
# dados ["nome4"] = input("Insira o seu nome: ")
# dados ["funcao4"] = input("Insira a sua função: ")
# dados["salario4"] = float(input("Digite o seu salário: "))
# print ("_"*30)
# salario = [dados["salario1"],dados["salario2"], dados["salario3"], dados["salario4"]]
# maiorsalario = max(salario)
# if maiorsalario == dados["salario1"]:
#     print(f'Funcionário {dados["nome1"]} tem o maior salário')
# if maiorsalario == dados["salario2"]:
#     print(f'Funcionário {dados["nome2"]} tem o maior salário')
# if maiorsalario == dados["salario3"]:
#     print(f'Funcionário {dados["nome3"]} tem o maior salário')
# if maiorsalario == dados["salario4"]:
#     print(f'Funcionário {dados["nome4"]} tem o maior salário')
l = []
maior = 0
for i in range (4):
    d = {}
    d["nome"] = input("Digite o seu nome: ")
    d["funcao"] = input("Digite a sua função: ")
    d["salario"] = float(input("Digite o seu salário: "))
    l.append(d)
    if d["salario"]> maior:
        maior = d["salario"]
for pessoa in l:
    if pessoa["salario"] == maior:
        print (f'Pessoa com maior salário é {pessoa["nome"]}')