import random

class BingoSorteio:
    def __init__(self):
        self.numeros_sorteados = []
    def sortear_numero(self):
        if len(self.numeros_sorteados) >= 75:
            print("Todos os números já foram sorteados.")
            return None
        while True:
            numero = random.randint(1, 75)
            if numero not in self.numeros_sorteados:
                self.numeros_sorteados.append(numero)
                print(f"Número sorteado: {numero}")
                return numero
    def exibir_numeros_sorteados(self):
        print(f"Números sorteados até agora: {sorted(self.numeros_sorteados)}")
bingo = BingoSorteio()
while len(bingo.numeros_sorteados) < 75:
    input("Pressione Enter para sortear um número...")
    bingo.sortear_numero()
    bingo.exibir_numeros_sorteados()