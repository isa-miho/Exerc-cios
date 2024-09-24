tipos = ['Higiene','Alimento','Produtos para pets']
higiene = ['10 - Shampoo','20 -Condicionador','30 -Sabonete','40 - Desodorante']
alimento = ['50 - Frios','60 - Carne','70 - Massa','80 - Legumes']
pet = ['90 - Ração','100 - Sache','110 - Brinquedo','120 - Acessório']
codigos = ('Shampoo: 10\nCondicionador: 20\nSabonete: 30\nDesodorante: 40\nFrios: 50\nCarne: 60\nMassa:70\nLegumes: 80\nRação: 90\nSache: 100\nBrinquedo: 110\nAcessório: 120')
carrinho = []
shampoo = 15
condicionador = 15
sabonete = 10
desodorante = 8
frios = 20
carne = 24
massa = 13
legumes = 12
racao = 9
sache = 7
brinquedo = 4
acessorio = 7
novoproduto = 0

Shampoo =  6.59
Condicionador = 5.98
Sabonete = 2.49
Desodorante = 9.98
Frios = 4.58
Carne = 17.78
Massa = 7.88
Legumes = 5.5
Racao = 24.45
Sache = 2.59
Brinquedo = 15.78
Acessorio = 13.45
novoProduto = 0
while True:
    print("Aperte 1 para funcionário\nAperte 2 para cliente") #Identificar o tipo de usuário
    credencial = int(input("Selecione a opção desejada: "))
    if credencial == 1:
         
        nome = input("Insira o nome do funcionário: ") #funcionário
        matricula = int(input("Digite o número de matricula: "))
        data = input("Data de nascimento: ")
        cpf = int(input("Insira o seu cpf: "))
        print (f'Bem vindo(a) {nome}!')
        while True:
            print ('E - Entrada no estoque')
            print ('A - Adicionar produto')
            print ('C - Consultar estoque')
            print ('P - Alterar preço de produto')
            print ('X - Sair')
            operacao = input('Insira a ação desejada: ')
            if operacao == "E": #entrada de produtos no estoque
                print(codigos)
                codigo = int(input('Digite o código do produto que deseja fazer entrada: '))
                E = int(input('Insira a quantidade de produtos que deseja fazer entrada: '))
                if codigo == 10:
                    shampoo += E
                elif codigo == 20:
                    condicionador += E
                elif codigo == 30:
                    sabonete += E
                elif codigo == 40:
                    desodorante += E
                elif codigo == 50:
                    frios += E
                elif codigo == 60:
                    carne += E
                elif codigo == 70:
                    massa += E
                elif codigo == 80:
                    legumes += E
                elif codigo == 90:
                    racao += E
                elif codigo == 100:
                    sache += E
                elif codigo == 110:
                    brinquedo += E
                elif codigo == 120:
                    acessorio += E
            if operacao == "A":
                print ('1 - Higiene\n2 - Alimentos\n3 - Produtos para pets')
                adicao = int(input("Digite o tipo de produto que deseja adicionar: "))
                if adicao == 1:
                    nomeProduto = input("Digite o nome do produto: ")
                    descricao = input("Adicione uma breve descrição do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    Codigos = int(input("Digite o código do produto: "))
                    novoProduto = int(input("Digite a quantidade de produtos: "))
                    higiene.append(Codigos)
                    higiene.append(nomeProduto)
                    higiene.append(preco)
                    novoProduto = preco
                    print ("Produto adicionado com sucesso")
                    break
                elif adicao == 2:
                    nomeProduto = input("Digite o nome do produto: ")
                    descricao = input("Adicione uma breve descrição do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    Codigos = int(input("Digite o código do produto: "))
                    novoProduto = int(input("Digite a quantidade de produtos: "))
                    alimento.append(Codigos)
                    alimento.append(nomeProduto)
                    alimento.append(preco)
                    novoProduto = preco
                    ("Produto adicionado com sucesso")
                    break
                elif adicao == 3:
                    nomeProduto = input("Digite o nome do produto: ")
                    descricao = input("Adicione uma breve descrição do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    Codigos = int(input("Digite o código do produto: "))
                    novoProduto = int(input("Digite a quantidade de produtos: "))
                    pet.append(Codigos)
                    pet.append(nomeProduto)
                    pet.append(preco)
                    novoProduto = preco
                    ("Produto adicionado com sucesso")
                    break
            if operacao == "C":
                print (f'Quantidade de shampoo no estoque: {shampoo}')
                print (f'Quantidade de condicionador no estoque: {condicionador}')
                print (f'Quantidade de sabonete no estoque: {sabonete}')
                print (f'Quantidade de desodorante no estoque: {desodorante}')
                print (f'Quantidade de frios no estoque: {frios}')
                print (f'Quantidade de carne no estoque: {carne}')
                print (f'Quantidade de massa no estoque: {massa}')
                print (f'Quantidade de legumes no estoque: {legumes}')
                print (f'Quantidade de ração no estoque: {racao}')
                print (f'Quantidade de sachê no estoque: {sache}')
                print (f'Quantidade de brinquedo no estoque: {brinquedo}')
                print (f'Quantidade de acessório no estoque: {acessorio}')
            if operacao == "P":
                print(codigos)
                codigo = int(input('Digite o código do produto que deseja alterar os preços: '))
                if codigo == 10:
                    Shampoo = float(input("Digite o novo preço: "))
                if codigo == 20:
                    Condicionador = float(input("Digite o novo preço: "))
                if codigo == 30:
                    Sabonete = float(input("Digite o novo preço: "))
                if codigo == 40:
                    Desodorante = float(input("Digite o novo preço: "))
                if codigo == 50:
                    Frios = float(input("Digite o novo preço: "))
                if codigo == 60:
                    Carne = float(input("Digite o novo preço: "))
                if codigo == 70:
                    Massa = float(input("Digite o novo preço: "))
                if codigo == 80:
                    Legumes = float(input("Digite o novo preço"))
                if codigo == 90:
                    Racao = float(input("Digite o novo preço: "))
                if codigo == 100:
                    Sache = float(input("Digite o novo preço: "))
                if codigo == 110:
                    Brinquedo = float(input("Digite o novo preço: "))
                if codigo == 120:
                    Acessorio = float(input("Digite o novo preço: "))
            if operacao == "X":
                print("Obrigado por usar o nosso sistema!")
                break
    if credencial == 2: #cliente
        nome = input("Insira o seu nome: ")
        cpf = int(input("Insira o seu cpf: "))
        print (f'Bem vindo(a) {nome}!')
        #preço dos produtos
        
        while True:
            print('1 - Comprar\n2 - Retirar produto do carrinho\n3 - Visualizar carrinho\n4 - Finalizar compra')
            acao = int(input("Escolha a ação desejada: "))
            if acao == 1:
                print ("Qual tipo de produto deseja comprar?")
                print ("1 - Higiene\n2 - Alimento\n3 - Produtos para pets")
                selecao = int(input("Escolha o tipo de produto: "))
                if selecao == 1:
                        print (higiene)
                        print(f'Shampoo: {Shampoo}\nCondicionador: {Condicionador}\nSabonete: {Sabonete}\nDesodorante: {Desodorante}')
                        compra = int(input("Digite o código do produto: "))
                        if compra == 10:
                            carrinho.append("Shampoo")
                        elif compra == 20:
                            carrinho.append("Condicionador")
                        elif compra == 30:
                            carrinho.append("Sabonete")
                        elif compra == 40:
                            carrinho.append("Desodorante")
                        elif compra == 130:
                            carrinho.append(nomeProduto)
                        else:
                            print("Código de produto inválido")
                if selecao == 2:
                        print(alimento)
                        print(f"Frios: {Frios}\nCarne: {Carne}\nMassa: {Massa}\nLegumes: {Legumes}")
                        compra = int(input("Digite o código do produto: "))
                        if compra == 50:
                            frios -= compra
                            carrinho.append("Frios")
                        elif compra == 60:
                            carne -= compra
                            carrinho.append("Carne")
                        elif compra == 70:
                            massa -= compra
                            carrinho.append("Massa")
                        elif compra == 80:
                            legumes -= compra
                            carrinho.append("Legumes")
                        elif compra == 130:
                            nomeProduto -= compra
                            carrinho.append(nomeProduto)
                        else:
                            print("Código de produto inválido")
                if selecao == 3:
                        print(pet)
                        print (f"Ração: {Racao}\nSache: {Sache}\nBrinquedo: {Brinquedo}\nAcessório: {Acessorio}")
                        compra = int(input("Digite o código do produto: "))
                        if compra == 90:
                            racao -= compra
                            carrinho.append("Racao")
                        if compra == 100:
                            sache -= compra
                            carrinho.append("Sache")
                        if compra == 110:
                            brinquedo -= compra
                            carrinho.append("Brinquedo")
                        if compra == 120:
                            acessorio -= compra
                            carrinho.append("Acessorio")
                        if compra == 130:
                            nomeProduto -= compra
                            carrinho.append(nomeProduto)
                        else:
                            print("Código de produto inválido")
            elif acao == 2:
                print ("Você está retiranto o último item adicionado no carrinho")
                retirado = carrinho.pop()
                print(f'{retirado} foi removido do carrinho.')
            elif acao == 3: 
                print (f'Você tem esses produtos no seu carrinho: {carrinho}')
            elif acao == 4: 
                        total = 0
                        #impostos
                        nacional = 0.05
                        estadual = 0.08
                        municipal = 0.12
                        for item in carrinho:
                            if item == "Shampoo":
                                total += Shampoo
                            elif item == "Condicionador":
                                total += Condicionador
                            elif item == "Sabonete":
                                total += Sabonete
                            elif item == "Desodorante":
                                total += Desodorante
                            elif item == "Frios":
                                total += Frios
                            elif item == "Carne":
                                total += Carne
                            elif item == "Massa":
                                total += Massa
                            elif item == "Legumes":
                                total += Legumes
                            elif item == "Racao":
                                total += Racao
                            elif item == "Sache":
                                total += Sache
                            elif item == "Brinquedo":
                                total += Brinquedo
                            elif item == "Acessorio":
                                total += Acessorio
                            elif item == nomeProduto:
                                total += novoProduto
                        for i in carrinho:
                            print (i)
                        qtdprodutos = len(carrinho)
                        print(f'O total da sua compra é: R${total:.2f}')
                        print ("Formas de pagamento:\n1 - Dinheiro\n2 - Cartão de crédito\n3 - Cartão de débito\n4 - Voucher alimentação\n5 - Pix")
                        pagamento = int(input("Escolha a forma de pagamento: "))
                        if pagamento == 1: #dinheiro
                            dinheiro = float(input("Digite o valor em dinheiro que será entregue: "))
                            if dinheiro>= total:
                                troco = dinheiro - total
                                nacional = (total * nacional)
                                estadual = (total * estadual)
                                municipal = (total * municipal)
                                print("_"*30)
                                print(f'Você comprou {qtdprodutos} produtos')
                                print (carrinho)
                                print("_"*30)
                                print (f'Seu total é: {total}')
                                print (f'Seus impostos foram:\nImposto nacional(5%): {nacional}\nImposto estadual(8%): {estadual}\nImposto municipal(12%): {municipal}')
                                print (f'Seu troco é {troco:.2f}')
                                print ("Obrigado por comprar em nossas lojas!")
                                break
                            else:
                                print ("Compra não autorizada\nEscolha outra forma de pagamento")
                        if pagamento == 2 or pagamento == 3 or pagamento == 5: #cartão ou pix
                            saldo = float(input("Digite o valor do seu saldo: "))
                            if saldo>= total:
                                senha = int(input("Digite a sua senha: "))
                                nacional = (total * nacional)
                                estadual = (total * estadual)
                                municipal = (total * municipal)
                                print("_"*30)
                                print(f'Você comprou {qtdprodutos} produtos')
                                print (carrinho)
                                print("_"*30)
                                print (f'Seu total é: {total}')
                                print (f'Seus impostos foram:\nImposto nacional(5%): {nacional}\nImposto estadual(8%): {estadual}\nImposto municipal(12%): {municipal}')
                                print ("Obrigado por comprar em nossas lojas!")
                                break
                            else:
                                print ("Compra não autorizada\nEscolha outra forma de pagamento")
                        if pagamento == 4: #Voucher
                            senha = int(input("Digite a sua senha: "))
                            print ("Obrigado por comprar em nossas lojas!\nO recibo logo será entregue")
                            nacional = (total * nacional)
                            estadual = (total * estadual)
                            municipal = (total * municipal)
                            print("_"*30)
                            print(f'Você comprou {qtdprodutos} produtos')
                            print (carrinho)
                            print("_"*30)
                            print (f'Seu total é: {total}')
                            print (f'Seus impostos foram:\nImposto nacional(5%): {nacional}\nImposto estadual(8%): {estadual}\nImposto municipal(12%): {municipal}')
                            print ("Obrigado por comprar em nossas lojas!")
                            break