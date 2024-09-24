import random
class BingoCartela:
    def __init__(self):
        self.cartela = self.gerar_cartela()
        self.numeros_marcados = set()
    def gerar_cartela(self):
        cartela = []
        colunas = {
            'B': (1, 15),
            'I': (16, 30),
            'N': (31, 45),
            'G': (46, 60),
            'O': (61, 75)
        }
        for key, (start, end) in colunas.items():
            numeros = random.sample(range(start, end + 1), 5)
            cartela.append(numeros)
        cartela[2][2] = "FREE"
        return cartela
    def exibir_cartela(self):
        headers = " B I N G O "
        print(headers)
        for i in range(5):
            for j in range(5):
                if self.cartela[j][i] == "FREE" or (j, i) in self.numeros_marcados:
                    print(" X ", end=" ")
                else:
                    print(f"{self.cartela[j][i]:2}", end=" ")
            print()
    def marcar_numero(self, numero):
        for i in range(5):
            for j in range(5):
                if self.cartela[j][i] == numero:
                    self.numeros_marcados.add((j, i))
    def verificar_bingo(self):
        for i in range(5):
            if all((i, j) in self.numeros_marcados or self.cartela[i][j] == "FREE" for j in range(5)):
                return True
            if all((j, i) in self.numeros_marcados or self.cartela[j][i] == "FREE" for j in range(5)):
                return True
        if all((i, i) in self.numeros_marcados or self.cartela[i][i] == "FREE" for i in range(5)):
            return True
        if all((i, 4 - i) in self.numeros_marcados or self.cartela[i][4 - i] == "FREE" for i in range(5)):
            return True
        return False
cartela = BingoCartela()
cartela.exibir_cartela()
while True:
    numero = int(input("Digite o número sorteado (ou 0 para sair): "))
    if numero == 0:
        break
    cartela.marcar_numero(numero)
    cartela.exibir_cartela()
    if cartela.verificar_bingo():
        print("Bingo!")
        break