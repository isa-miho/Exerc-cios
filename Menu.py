carrinho = []
while True:
    menu = int(input("Digite a opção que desejada: Adicionar produto-1, Visualizar o carrinho-2, Finalizar compra-3 "))
    if menu == 3:
        break
    if menu== 1:
        print ("1 - Ameixa","\n2 - Batata","\n3 - Chocolate")
        compra = int(input("Digite o código do produto: "))
        if compra == 1:
            carrinho.append("Ameixa")
        if compra == 2:
            carrinho.append("Batata")
        if compra == 3:
            carrinho.append("Chocolate")
    elif menu == 2:
        print (f'Produtos:{carrinho}')
