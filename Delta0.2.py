a = float(input("Digite o valor de a: "))
if a == 0:
    print ("Não é equação do segundo grau. ")
    exit()
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = ((b)**2 - 4*a*c)**0.5
if delta == 0:
    print ("A equação tem apenas uma raiz real")
    exit()
elif delta<0:
    print ("Não existem raizes reais nesta equação")
    exit()
elif delta>0:
    print ("A equação possui 2 raizes reais")
    x1 = ((-(b) + delta)/2*a)
    x2 = ((-(b) - delta)/2*a)
    print (f'As raízes são: x1= {x1} e x2= {x2}')
